"""
Print Only Important Fields from Ollama Response
===============================================

Shows key metadata + performance + output text.
"""

from typing import Dict, Any
import ollama

NS_TO_SEC = 1_000_000_000  # nanoseconds → seconds


def print_ollama_summary(response: Dict[str, Any]) -> None:
    """Print a clean summary of Ollama generation response."""

    # -------- Basic Info --------
    model = response.get("model")
    done = response.get("done")
    reason = response.get("done_reason")

    print(f"Model Used        : {model}")
    print(f"Completed         : {done}")
    print(f"Stop Reason       : {reason}")

    # -------- Performance --------
    total_ns = response.get("total_duration", 0)
    eval_ns = response.get("eval_duration", 0)
    token_count = response.get("eval_count", 0)

    total_sec = total_ns / NS_TO_SEC
    eval_sec = eval_ns / NS_TO_SEC
    tps = (token_count / eval_sec) if eval_sec else 0 # tokens per sec, with zero error handling

    print(f"Total Time (sec)  : {total_sec:.2f}")
    print(f"Gen Time (sec)    : {eval_sec:.2f}")
    print(f"Output Tokens     : {token_count}")
    print(f"Tokens/sec        : {tps:.2f}")

    # -------- Output --------
    text = response.get("response", "")
    print("\nModel Response:\n")
    print(text)


def main() -> None:
    response = ollama.generate(
        model="llama3.2:1b",
        prompt="why are leaves green?"
    )

    print_ollama_summary(response)


if __name__ == "__main__":
    main()


# Output
'''
Model Used        : llama3.2:1b
Completed         : True
Stop Reason       : stop
Total Time (sec)  : 9.72
Gen Time (sec)    : 6.97
Output Tokens     : 291
Tokens/sec        : 41.73

Model Response:

Leaves appear to be green because they contain a pigment called chlorophyll, which is responsible for absorbing light energy from the sun. Chlorophyll is present in the cells of most leaf tissues and reflects blue and red light, while passing mostly green light on through.

When sunlight hits a leaf, it excites the electrons in the chlorophyll molecules, causing them to absorb light energy and convert it into chemical energy. This energy is then used to power the conversion of carbon dioxide and water into glucose and oxygen through the process of photosynthesis.

The green color of leaves is also influenced by other pigments that are present in certain types of plants. These include:

* Carotenoids: These are yellow, orange, or brown pigments that are responsible for the autumn colors of leaves as they change with the seasons.
* Anthocyanins: These are red or purple pigments that are produced during the fall months when the trees stop producing chlorophyll and the sugars in the leaves become concentrated.
* Betalains: These are yellow or orange pigments that are found in some plants, such as beets and Swiss chard.

So, to summarize, the green color of leaves is due to the presence of chlorophyll, which absorbs light energy and reflects blue and red light. Other pigments can also contribute to the overall color of a leaf, but they do not affect the basic green color that chlorophyll provides.
'''

# ============================================
# ============================================
# ============================================

# Summary:
'''
OLLAMA RESPONSE SUMMARY UTILITY — KEY POINTS
============================================

✅ PURPOSE
- Extract only important metadata + performance metrics + model text
- Avoid printing full raw response (too noisy)
- Useful for benchmarking local LLM inference

---------------------------------------------
🧠 RESPONSE STRUCTURE UNDERSTANDING
---------------------------------------------
Important Ollama response fields:

- model           → model name used
- done            → whether generation finished
- done_reason     → why generation stopped
- total_duration  → total pipeline time (ns)
- eval_duration   → actual token generation time (ns)
- eval_count      → number of output tokens
- response        → generated text

---------------------------------------------
⚡ PERFORMANCE METRICS (VERY IMPORTANT)
---------------------------------------------
1) Nanoseconds → Seconds conversion
   - Ollama durations are in nanoseconds
   - Convert using:
        seconds = nanoseconds / 1e9

2) Total Time
   - End-to-end latency
   - Includes preprocessing + generation + overhead

3) Generation Time
   - Pure token decoding time
   - Best indicator of model speed

4) Tokens/sec
   - Throughput metric
   - tokens/sec = eval_count / eval_duration_sec
   - Used for comparing models & hardware

---------------------------------------------
🎯 DESIGN QUALITY OBSERVATIONS
---------------------------------------------
✔ Defensive access using .get()
✔ Clear logical sections (Basic / Perf / Output)
✔ Central constant for unit conversion
✔ Division-by-zero safety
✔ Clean formatted output
✔ Reusable utility function

---------------------------------------------
🚀 WHY THIS IS INDUSTRY-RELEVANT
---------------------------------------------
- Backend observability for LLM calls
- Performance benchmarking (model vs model)
- Hardware comparison (CPU vs GPU)
- Latency monitoring
- Logging for production agents

---------------------------------------------
⭐ CORE TAKEAWAY
---------------------------------------------
Raw LLM responses are verbose.
Real systems extract → summarize → log → monitor.

This function is exactly that layer.
'''