"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": "02:30",
            "answer": 105.0
        },
        {
            "input": "18:00",
            "answer": 180.0
        },
        {
            "input": "12:01",
            "answer": 5.5
        },
        {
            "input": "00:00",
            "answer": 0.0
        },
        {
            "input": "01:43",
            "answer": 153.5
        },
        {
            "input": "01:42",
            "answer": 159.0
        },
        {
            "input": "13:42",
            "answer": 159.0
        },
        {
            "input": "23:59",
            "answer": 5.5
        },
    ],
    "Extra": [
        {
            "input": "05:40",
            "answer": 70.0
        },
        {
            "input": "05:16",
            "answer": 62.0
        },
        {
            "input": "20:37",
            "answer": 36.5
        },
        {
            "input": "00:23",
            "answer": 126.5
        },
        {
            "input": "23:47",
            "answer": 71.5
        },
        {
            "input": "07:01",
            "answer": 155.5
        },
        {
            "input": "13:50",
            "answer": 115.0
        },
        {
            "input": "19:27",
            "answer": 61.5
        },
        {
            "input": "04:03",
            "answer": 103.5
        },
        {
            "input": "14:55",
            "answer": 117.5
        },
    ]
}
