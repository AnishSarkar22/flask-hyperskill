# Python Backend with Flask Notes

## Python Notes

1. A dynamic array is a linear data structure. Elements can be added/removed/moved in dynamic array. Main properties are: size, and capacity.
2. Time complexity of adding an element is O(n), updating is O(1), removing is O(n).
3. If dynamic array exceeds its capacity, all elements will be copied to a new internal array of a bigger size.
4. If scaling factor of dynamic array is x, then when the array fills to max capacity, the new capacity will multiply by x of the previous capacity and not the initial capacity.
5. Assume you have a dynamic array with an initial size and capacity of 2, and the scaling factor is 2. What is the minimum number of additional elements you need to insert to increase the capacity to 1024? ANS: 511 (1024-free_capacity/scaling_factor).
6. *args: Used to pass a variable number of positional arguments (i.e., unnamed arguments).
7. **kwargs: Used to pass a variable number of keyword arguments (i.e., named arguments).
8. Python encourages using default arguments and variable-length arguments **(\*args and \*\*kwargs)** to achieve similar functionality as method overloading.
9. Docstring: It is a string literal. It is written as the first statement in the definition of a module, a class, a method, a function, etc., and briefly describes its behavior and how you can use it, what parameters you should pass to the function. Two types of docstrings are: one-liners and multi-liners.
10. Under PEP 257, you should follow the next conventions for docstrings for functions and methods:
       1. The opening and the closing quotes should be on the same line.
       2. There should be no empty strings either before or after the docstring.
       3. Your description should be imperative, that's why we need the wordings like """Return the factorial.""" or """Return the number.""" instead of """Returns the number.""" or """It returns the number.""".
       4. The description is not a scheme that repeats the object's parameters and return values, like """count_factorial(num) -> int.""".
11. If backslash is contained in a docstring then we should use *r* prefix such as `r"""A \new example with \triple double-quotes."""`
12. A set is an unordered container of hashable objects.
13. Immutable data types can be elements of a set. They **do not** record element position. `set()` function is used to void repetitions.
14. The only difference between `set` and `frozenset` is that set is a mutable data type, but frozenset is not. To create a frozenset, we use the `frozenset()` function.
15. Python does not support method overloading as it is a dynamically typed language, meaning that variables types are determined at runtime rather than compile-time.
16. Inheritance:

                  # inheritance syntax
                  class ChildClass(ParentClass):
                        # methods and attributes
                        ...
       Here, ChildClass is the subclass of ParentClass. Inheritance can be of 2 types: **Single** and **Multiple**
17. We can check type of an object by using `type(object) or type(object, bases, dict)` and `isinstance(object, type)`. `isinstance(object, type)` allows us to check for the immediate type of object but also with the parent type and also it would work with the parent of parent type [consider inheritance] whereas `type(object)` only allows us to check for the immediate type of the object [does not consider inheritance].
18. `type(object)` checks for the exact type of the object, while `isinstance(object, type)` checks if the object is an instance of a class or its subclass.
19. **Overriding:** Any object-oriented programming language can allow a subclass or child class to offer a customized implementation of a method already supplied by one of its superclasses or parent classes.
20. super(): Used to give access to methods and properties of a parent or sibling class. Returns an (proxy,or temporary) object of the parent class. Example: See super_method.py, super_method2.py,super_method3.py file.
21. Functions in `os` module:
      1. `os.getcwd()` to learn (or gets) the current working directory and `os.chdir()` to change it.
      2. `os.mkdir()` to create a single directory and `os.makedirs()` to create nested folders.
      3. `os.listdir()` to get listing of the directory's content and `os.rename()` to create the name of files and folders.
22. **unittest module:** Tool for writing tests. `unittest.TestCase` class has different methods: <br>
        1.  `assertEqual(a, b)` => a == b <br>
        2.  `assertNotEqual(a, b)` => a != b <br>
        3.  `assertTrue(x)` => bool(x) is True <br>
        4.  `assertFalse(x)` => bool(x) is False <br>
        5.  `assertIsNone(x)` => x is None <br>
        6.  `assertIsNotNone(x)` => x is not None <br>
        7.  `assertGreater(a, b)` => a > b <br>
        8.  `assertLess(a, b)` => a < b <br>
        9.  `assertIsInstance(a, b)` => isinstance(a, b) <br>
        10. `assertRaises(exception, function, arguments)` => Raises the exception when given the arguments
23. `setUp()` method is executed *before every* test method and the code inside.
24. `tearDown()` method is executed *after every* test method.
25. We can get details for each test method by typing `-v`, or stop the tests after the first failure or error by typing `-f` in the command line.
26. Unpacking Operators: THese are at the left of `=` operator. Using single asterik (*) or double asteriks (**) we can unpack elements from tuple, lists, dictionaries. Double can get *values* of dictionary but single can get only *keys*. See Unpacking.py for more.
27. Context Managers: Used to close the files opened at right time and also release the descriptor when done using the file.
28. Types of tests are:
        1.  Unit tests: Tests for components at a low level in an isolated manner, like a class method. These can be automated and it is recommended to have a lot of unit tests for different components.
        2.  Integration tests: Tests to verify two or more components or services work well together.
        3.  Functional tests: Tests two or more components, but focus on the business requirements of the application. These tests are similar to integration tests but they are expected to be correct from a functional point of view.
        4.  End-to-End tests: Tests the application from a user point of view in an application environment, these are expensive to run when automated and it is recommended to have minimum required E2E tests.
        5.  Regression tests: Regression tests are a combination of functional and non-functional tests that you run when the software has some changes. They validate that new software is not breaking existing functionality. Choose them carefully as they determine the time spent in testing in many cases.
        6.  Performance tests: Tests that evaluate the performance of a software system under a specific workload. These tests help to measure the scalability, reliability, and responsiveness of an application. It can determine if an application meets performance requirements, locate bottlenecks and measure stability during peak traffic.
        7.  Acceptance tests: These tests involve everything that is needed to get the software accepted. These may be functional tests, E2E tests, and performance tests. These tests are formally defined and can be used as a criterion for decision-making on software adoption.
29. Best practices for `pytest` are:
        1.  Store all tests in a `tests/` directory
        2.  File names should strictly start with `test_`
        3.  Function names should strictly start with `test`
30. Requests in Python:
        1.  `requests.post()`: A POST request allows you to send some additional data to the server. Unlike GET requests, where you could specify additional parameters in the query string, POST requests pass additional data in the **body** of the message (request). Example: `r = requests.post('http://bestblogever.com/posts', data=data)`
        2.  `requests.put()`: PUT method replaces the resource at the given URL with the resource specified within the request. If there is originally no resource to replace on the server, PUT will create one. Example: `r = requests.put('http://bestblogever.com/posts/<post_id>', data=data)`
        3.  `requests.delete()`: You might also want to remove a post from your blog. In order to do so, you'll need to send a DELETE request, which deletes the resource identified by the request URL. Example: `r = requests.delete('http://bestblogever.com/posts/<post_id>')`
31. 

## Web Technologies Notes

1. Standard Status codes:
         1. 1xx: Informational
         2. 2xx: Success
         3. 3xx: Redirection
         4. 4xx: Client Error
         5. 5xx: Server Error
2. HTTP Methods: GET, POST, HEAD
3. **REST (Representational State Transfer):** REST is NOT a protocol or a standard. REST usually works on top of HTTP and is one of the possible ways to use HTTP. It is not a standard, but rather a set of useful recommendations. A service (or app) that follows REST rules is called **RESTful**.
4. 6 **REST** principles:
          1. Client-server interaction model
          2. Stateless
          3. Cacheable
          4. Uniform interface
          5. Layered system
          6. Code on demand [optional]
5. HTTP methods for RESTful services:
          1. POST => To create new resources.
          2. GET => Retrieve or read the resource.
          3. PUT => Either creates a resource by the specified ID or updates an existing one.
          4. DELETE => To remove a resource identified by a specific URI (ID).
6. `wget` is installed on most linux distros.
7. `curl` can upload files to the server.
8. `curl` and `wget` can download files from the internet.
9.  Advantages of `wget` and `curl`:
          1. Can access quite some advanced features, not available otherwise.
          2. With `wget` and `curl` you can check the file integrity and trustworthiness by verifying the checksum.
          3. You can also automatically set the amount of time you are ready to wait or how many times you want to retry the request.
10. Disadvantages of `wget` and `curl`:
          1. They require you to already know the URL from where you want to download the file.
          2. It takes time to practice knowing them well.
11. **Idempotency** is an important concept of some HTTP requests. A request is called idempotent if sending the same request more than once doesn't introduce additional changes to the state of the server. `GET`, `PUT`, `DELETE` are idempotent. `POST` is not idempotentbecause a POST request may add new data to the server.
12. There are two versions of the IP protocol:
        1.  IPv4: consists of four numbers from 0 to 255 separated by dots. uses a 32-bit value for its Internet addresses, it means that the protocol can provide support for 2^32 IP addresses in total that is equal to around 4.29 billion various addresses. Example: 132.245.4.216
        1.  IPv6: uses 128 bits to represent an address that allows for 2^128 different addresses. Example: 0de2:041a:7d43:65ab:9a63:a63e:aa78:34c2
13. **Loopback addresses:** There are special IP addresses that point to the local computer, that is, the computer you are using right now. They are called loopback addresses. They are useful when you want to connect to a server on your computer.

## UI Notes

1. Features of UX:
      1. Interaction Design
      2. Wireframes & Prototypes
      3. Information Architecture
      4. Senarios
      5. Focus on Interactions
2. Features of UI:
      1. Visual Design
      2. Color Palette
      3. Layouts
      4. Typography
      5. Focus on Tools
3. Layout Grids: Grids use columns to mark up the screen and margins to measure the distance from the edge of the screen. Gutters are also used between columns to visually separate elements from each other, such as ensuring that buttons don't overlap.
4. Common Layout Grids: ScrollView, FrameLayout, RelativeLayout, GridLayout.

## Flask Notes

1. `make_response` function which handles simple responses. It is an instance of the `Response` class.
2. `jsonify` function is used to convert Python objects (like dictionaries or lists) into proper JSON responses. **jsonify** automatically sets the Content-Type header of the response to 'application/json'. This tells the client that the response body contains JSON data.
3. Routes: Flask uses decorators. Example of routes- `@app.route('/')`
4. Query Parameters: Code for the example(http://127.0.0.1:5000/users?city=London&age=20):

                                    @app.route('/users')
                                    def users():
                                          query_params = request.args  # returns a dictionary
                                          city = query_params.get("city")
                                          age = query_params.get("age")
                                          # ... do your magic with the params
                                          # considering you've had the predefined method 'get_users' for retrieving users
                                          result = get_users(city, age)
                                          return result

5. **Jinja2:**
      1. {% ... %} : conditional and looping statements like if, for are enclosed within a string that starts a block {% and one that ends it %}.
      2. {{ ... }}: variables are enclosed within variables that start {{ and end }} a string. With their help, the value of a variable can be printed to the template output.
      3. {% if flag %}
6. **Redirects:** Example: see redirect.py file
7. Flash Messages/ pop-ups: We can pass a category to the flash method to indicate that the message belongs to a specific type. For example, if you want to notify users that they are looking at the site for 5 hours straight, you can use the info category. If you want to tell your users that they don't have the right to do something, use error. Example: see popups.py


## SQL Notes

1. E-R diagrams: used for visual display of the structure of relational database: **entity**,**relationship** and **attribute**.
2. Levels of database design:
      1. Conceptual (semantic): structure is clear and understadable for all users, developers and customers.
      2. Logical: Structure is converted to some model (most often relational). In many CASE (computer aided software engineering)tools, the conceptual and logical layers are combined.
      3. Physical: DB model is presented in the form in which it should be described in a specific DBMS. For example, archar2 – oracle.
3. Types of keys:
      1. Primary key: uniquely defines the entity (for each row in the table it is different / cannot be repeated). For example, a passport number.
      2. Foreign key: It is the primary key of one entity, which is needed to communicate with another entity (it can be repeated).
4. Different types of connections:
      1. one-to-one (1-1): for example, passport-citizen
      2. one-to-many (1-M): for example, student-group
      3. many-to-many (M-M): for example, student-subjects
5. Different types of links:
      1. identifying (solid line): Primary key of one entity (main) goes into the primary key, which is also a foreign key to another entity (dependent). Dependent entities are those entities that depend on other entities (parent/main). For example, a citizen (dependent) cannot exist without a passport (main).
      2. non-identifying (dashed line): Primary key of one entity does not go into the primary key of another entity but becomes a non-key attribute (like a foreign key). For example, a student and a group: the student may not have a group number assigned.
6. Normalization: improving the properties of a database by sequentially dividing one table into several tables. Reason is presence of anomalies in unnormalized database. (An anomaly is a situation in which there is a complication of data processing and a violation of consistency, i.e. the correctness or adequacy of information storage)
7. Types of normal forms:
      1. First normal form (1NF): When all data in its cells are atomic i.e simple and non-separable.
      2. Second normal form (2NF): It is based on **functional dependance**. It is more of a semantic concept and is denoted as **x->y** (read as x functionally defines y, or y is functionally dependent on x). For example, x1->y1, x1->y2 then y1 = y2. Here x is **dependency determinant**.
8. Object Mapping: The structure of data in the source system may be different from the structure of data in the destination system. 