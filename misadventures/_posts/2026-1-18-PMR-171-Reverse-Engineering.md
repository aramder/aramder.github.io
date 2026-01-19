---
layout: post
category: misadventures
title: AI-Assisted Reverse Engineering of the PMR-171
---

![PMR-171 portable radio](/images/PMR171/pmr171_radio.png)

I picked up a Guohetec PMR-171 wideband portable radio a few months ago. It's a compact manpack-style transceiver—roughly double the size of a Yaesu FT-817, or comparable to a typical 100W rig—covering HF through UHF with FM, AM, SSB, and even DMR support. The problem? The manufacturer's programming software has limited capabilities and is completely undocumented. Coming from other radios with proper CPS (Customer Programming Software), I wanted to understand how this one worked.<!--more-->

So I reverse engineered the programming protocol. Well, *I* didn't do it—an LLM did. I captured UART traffic, fed it to an AI for pattern analysis, reported test results, and iterated. The AI handled hex parsing, protocol documentation, and building lookup tables. The result is a complete understanding of the radio's serial protocol and codeplug format.

## The Challenge

Reverse engineering a proprietary protocol typically involves:

- **~15 UART capture files** from various programming operations
- **50 CTCSS tone mappings** requiring brute-force discovery
- **40+ JSON fields** to decode and document
- **Packet structure analysis** (headers, commands, checksums)
- **Systematic testing** to validate findings

The kind of work I'd normally estimate at "a few weekends" and never actually finish.

## Why This Worked

Reverse engineering involves a specific category of work that AI handles well:

| Task Type | Human Effort | AI Effort |
|-----------|--------------|-----------|
| Pattern matching in hex dumps | Tedious, error-prone | Fast, consistent |
| Iterative test-analyze-adjust cycles | Time-consuming | Rapid iteration |
| Documentation maintenance | Often neglected | Automatic |
| Boilerplate code generation | Mind-numbing | Effortless |
| Protocol specification writing | Avoided | Thorough |

The individual tasks aren't hard. They're just numerous and boring. I wouldn't have written 24 JSON validation tests manually. I wouldn't have documented every field in the protocol. I definitely wouldn't have mapped all 50 CTCSS tones through brute-force testing.

## The UART Protocol

The first challenge was figuring out how the radio communicates. No documentation exists. The manufacturer software is a black box.

**Discovery process:**
1. Capture UART traffic during factory software operations
2. Feed captures to AI for pattern analysis

![Serial monitor capture showing UART traffic](/images/PMR171/serial_monitor.png)

3. Identify packet structure (header, length, command, payload, checksum)
4. Implement and test individual operations
5. Build complete read/write driver

**Key finding that took hours to discover:** The radio won't respond unless both DTR and RTS serial control signals are set HIGH. This isn't documented anywhere. The AI tried various approaches, I reported failures, and eventually we narrowed it down through systematic elimination.

```python
# The critical detail
ser = serial.Serial('COM3', 115200)
ser.dtr = True  # Required!
ser.rts = True  # Also required!
```

The protocol turned out to be straightforward once we found the right parameters:

```
┌────────┬────────┬────────┬─────────────┬──────────┐
│ Header │ Length │ Cmd ID │ Payload     │ Checksum │
│ (2 B)  │ (1 B)  │ (1 B)  │ (Variable)  │ (1 B)    │
└────────┴────────┴────────┴─────────────┴──────────┘
```

## The CTCSS Mapping Problem

CTCSS (Continuous Tone-Coded Squelch System) tones are sub-audible tones used for selective calling. The radio supports 50 standard tones. In the codeplug, these aren't stored as frequencies—they're stored as arbitrary index values in fields called `emitYayin` and `receiveYayin`.

The mapping is:
- Non-linear (not sequential)
- Undocumented
- Contains random gaps (indices 25, 45, 47, 51, 53 are unused)

| Position | Frequency | Index |
|----------|-----------|-------|
| 1 | 67.0 Hz | 1 |
| 2 | 69.3 Hz | 2 |
| ... | ... | ... |
| 25 | 146.2 Hz | 24 |
| 26 | 151.4 Hz | 26 ← *gap at 25* |
| ... | ... | ... |
| 43 | 218.1 Hz | 46 |
| 44 | 225.7 Hz | 48 ← *gap at 47* |

To build a complete mapping:
1. Set tone on radio via manufacturer software
2. Read codeplug via UART
3. Extract `yayin` value
4. Repeat 50 times

Estimated manual time: 2.5 hours of clicking through menus. I would have mapped maybe 10 common tones and called it done.

**What actually happened:** Over 11 test iterations, the AI:
- Generated test configurations
- Analyzed UART captures
- Extracted yayin values
- Identified the non-linear pattern
- Built complete lookup tables
- Documented everything

**Test 11 validation result: 25 test channels, 100% accuracy.** Split tones, TX-only, RX-only—all confirmed functional.

![CTCSS validation - manufacturer software showing programmed tones read back from radio](/images/PMR171/ctcss_validation.png)

```python
CTCSS_TO_YAYIN = {
    67.0: 1,   69.3: 2,   71.9: 3,   74.4: 4,   77.0: 5,   
    79.7: 6,   82.5: 7,   85.4: 8,   88.5: 9,   91.5: 10,
    94.8: 11,  97.4: 12,  100.0: 13, 103.5: 14, 107.2: 15,
    110.9: 16, 114.8: 17, 118.8: 18, 123.0: 19, 127.3: 20,
    131.8: 21, 136.5: 22, 141.3: 23, 146.2: 24, 151.4: 26,
    156.7: 27, 159.8: 28, 162.2: 29, 165.5: 30, 167.9: 31,
    171.3: 32, 173.8: 33, 177.3: 34, 179.9: 35, 183.5: 36,
    186.2: 37, 189.9: 38, 192.8: 39, 196.6: 40, 199.5: 41,
    203.5: 42, 206.5: 43, 210.7: 44, 218.1: 46, 225.7: 48,
    229.1: 49, 233.6: 50, 241.8: 52, 250.3: 54, 254.1: 55
}
```

## Validation

The hardware validation script tests actual radio communication:

```bash
python tests/test_uart_read_write_verify.py --port COM3 --channels 5 --yes
# PMR-171 UART Read/Write Verification Test
# ========================================
# Channel 15: PASS
#   Mode: NFM → NFM ✓
#   Name: "TEST-CH-15" → "TEST-CH-15" ✓
#   Freq: 146.520000 → 146.520000 ✓
# [Results: 5/5 passed]
```

The AI also generated 24 automated tests validating JSON format compatibility with the manufacturer's software. I wouldn't have written a comprehensive test suite for a personal project, but now I have confidence the protocol implementation actually works.

## What I Actually Did

My contribution was:
- **Direction**: "Reverse engineer the PMR-171 protocol"
- **Hardware**: Connected the radio, captured UART traffic, ran tests
- **Review**: Verified findings against actual radio behavior
- **Iteration**: "That didn't work, try X instead"

The AI handled:
- Hex dump parsing and pattern recognition
- Protocol structure analysis
- Test configuration generation
- Lookup table construction
- Documentation

This isn't automation in the traditional sense. It's more like having a very fast, very patient assistant who never gets bored of staring at hex dumps and doesn't cut corners on documentation.

## Reflections

This project demonstrates something I've suspected for a while: there's a category of technical work that's straightforward but tedious, and AI tools are excellent at it.

| What AI Did Well | What Still Required Human |
|------------------|---------------------------|
| Hex dump analysis | Hardware access |
| Pattern recognition | Interpreting failures |
| Brute-force mapping | Domain knowledge |
| Documentation | "Try DTR=True" intuition |
| Test generation | Architectural decisions |

I now have complete protocol documentation for a radio that would otherwise remain a black box. Not because the reverse engineering was hard, but because the *work* wasn't interesting enough to justify the time investment manually.

All findings—packet structure, field mappings, CTCSS lookup tables—are documented in the repository. The resulting programming software will be covered in a future post.

## Resources

- **Repository**: [PMR_171_CPS](https://github.com/aramder/PMR_171)
- **UART Protocol Report**: [UART_Reverse_Engineering_Report.md](https://github.com/aramder/PMR_171/blob/main/docs/UART_Reverse_Engineering_Report.md)
- **CTCSS Mapping Table**: [Complete_Ctcss_Mapping.md](https://github.com/aramder/PMR_171/blob/main/docs/Complete_Ctcss_Mapping.md)
- **Protocol Specification**: [Pmr171_Protocol.md](https://github.com/aramder/PMR_171/blob/main/docs/Pmr171_Protocol.md)

---

*Disclaimer: This post was authored by AI. While the technical findings have been validated against real hardware, do not blindly trust anything written here—verify independently before relying on it for your own projects.*
