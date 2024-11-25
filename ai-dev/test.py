import requests

# Define test cases
test_cases = [
    # Same subject with minor variations
    {
        "student_answer": "The operating system protects resources by requiring user authentication, access control, and isolating processes to maintain system integrity.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    {
        "student_answer": "Operating systems use methods like authentication and encryption to secure data, along with permissions to restrict file access.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    {
        "student_answer": "Security is achieved using firewalls and antivirus software, protecting the system from external threats.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    {
        "student_answer": "User authentication protects files and processes from interference.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    {
        "student_answer": "Operating systems are responsible for running applications and managing hardware like the CPU and memory.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    # Identical answers
    {
        "student_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    # Different subjects
    {
        "student_answer": "Photosynthesis is the process by which plants use sunlight to synthesize food from carbon dioxide and water.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    {
        "student_answer": "Einstein's theory of relativity explains the relationship between space and time and how they interact with gravity.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    {
        "student_answer": "In programming, recursion is a method where the solution to a problem depends on solutions to smaller instances of the same problem.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    # Random strings
    {
        "student_answer": "asdfg hjklqwer tyuiop zxcvb nm",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    {
        "student_answer": "1234567890",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    {
        "student_answer": " ",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    #Computer networks
    {
        "student_answer": "In networking, packets are transmitted through different layers for error detection and delivery assurance.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    {
        "student_answer": "The OSI model is a framework for how applications communicate over a network in seven layers.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    {
        "student_answer": "The network layer of the OSI model routes packets from the source to the destination.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },

    # High-Performance Computing
    {
        "student_answer": "HPC utilizes distributed computing and parallel processing to solve computationally intensive tasks efficiently.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    {
        "student_answer": "High-performance computing accelerates simulations in scientific research using supercomputers.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    {
        "student_answer": "Clustering is a key concept in HPC, combining multiple nodes to act as a single powerful system.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },

    # Java
    {
        "student_answer": "Java is object-oriented and supports features like inheritance, polymorphism, and encapsulation.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    {
        "student_answer": "The Java Virtual Machine (JVM) allows code written in Java to run on any platform supporting JVM.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
    {
        "student_answer": "In Java, the garbage collector manages memory by automatically reclaiming unused objects.",
        "teacher_answer": "The Operating System ensures security and protection of resources through user authentication, access control, and encryption. It isolates processes to maintain system integrity.",
    },
]

# API endpoint
url = "http://127.0.0.1:8000/evaluate"

# Send requests and print responses
for i, case in enumerate(test_cases):
    response = requests.post(url, json=case)
    print(f"Test Case {i + 1}:")
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}, {response.text}")
    print("-" * 40)
