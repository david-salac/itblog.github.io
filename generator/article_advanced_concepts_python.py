# More about some useful concepts in the Python language
import datetime
import crinita as cr

lead = """Many helpful tools available in Python are essential for effective development - some of them are less known, others are way more popular. This article presents class methods and static methods (constructs of Python), conversion from class to dictionary (and vice versa) and metaclasses and their applications. All these things are vital for beginners and mid-senior Python engineers."""

content = """Many helpful tools available in Python are essential for effective development - some of them are less known, others are way more popular. This article presents class methods and static methods (constructs of Python), conversion from class to dictionary (and vice versa) and metaclasses and their applications. All these things are vital for beginners and mid-senior Python engineers.

<h2>Class and static methods (and fields)</h2>
<p>There are two beneficial concepts in Python language called class and static method. The class method is declared using the following declaration:</p>
<pre class="code"><code>@classmethod
def some_class_method(cls, arg1, arg2...): ...</code></pre>
<p>The first parameter of each class method is the type of class where the method is defined - this differs from the standard (undecorated) methods, which takes instance instead - using parameter usually called <code>self</code>. Class methods are useful if you want to create some class instance following a specific design pattern (like singleton) or when the method is dealing only with class fields (and not with the class instance). If you are familiar with languages like Java or C#, both static and class methods in Python are just static methods in Java. </p>
<p>A very similar concept to a class method is a static method. It differs only slightly:</p>
<pre class="code"><code>@staticmethod
def some_static_method(arg1, arg2): ...</code></pre>
<p>As you can see, there is no parameter <code>cls</code> present. Which is the only difference - otherwise, the static method behaves in the same way. Static methods are not needed very often (since they should not interact with any class field). If there is any interaction with class fields, you should prefer a class method.</p>

<h2>A bit more about dictionaries and classes</h2>
<p>There can be many good reasons to convert some (class) object to a dictionary (where each field of the object is accessible using logic <code>obj['field']</code>) and vice versa.</p>

<h3>Conversion from dict to class (and) object (using <code>collections.namedtuple</code>)</h3>
<p>A named tuple is a very helpful tool. It basically creates a (sub)class with required fields. It is helpful if you want to create a generic type besides the dictionary object (where dictionary keys are fields in this type). Consider the following example (we suppose that dictionary to be converted is variable <code>some_dict</code>):</p>

<pre class="code"><code># Create a type that contains fields equals to keys of dict
SuperType = collections.namedtuple(
    "SomeType", some_dict.keys()
)
# Create concrete object
obj_from_dict = SuperType(**some_dict)
# Now you can access fields:
obj_from_dict.some_key  # get the value some_dict['some_key']</code></pre>

<p>There is a much simpler conversion in the case that you do not need a type but just an object:</p>

<pre class="code"><code># Create object:
some_obj = types.SimpleNamespace(**some_dict)
# Now you can access fields:
some_obj.some_key  # get the value some_dict['some_key']</code></pre>
<p>The logic of this conversion is the same as above (dictionary keys are now fields of the object).</p>

<h3>Conversion of classes to dictionaries</h3>
<p>This is the opposite direction to the one presented above. Our ultimate goal is to convert object using logic: <code>some_dict = dict(obj)</code>. The key to success is to define methods <code>__getitem__</code> and keys in the object. A method called keys defines which class fields will be serialized to a dictionary. Method <code>__getitem__</code> defines serialization (accessing values using keys). Consider the following example:</p>

<pre class="code"><code>class SomeClass(object):
    something_1: str
    something_2: str
    def keys(self) -> List[str]:
        return ['something_1', 'something_2']
    def __getitem__(self, key):
        return getattr(self, key)

obj = SomeClass()
some_dict = dict(obj)  # convert classes object to dictionary</code></pre>

<p>You can also use the keyword <code>dir</code> or <code>vars</code> to get a list of classes variables.</p>

<h2>Something about multiple inheritance</h2>
<p>Python is a language that does not limit the number (and type) of classes from which another class can inherit. That allows you to do useful things like writing mixins (particularly helpful for unit-test classes), but it can naturally cause some issues. For example, this happens if some method (or variable) is declared in multiple parent classes (having the same name in each parent class).</p> 

<h3>Python MRO (Method Resolution Order)</h3>
<p>Python way to deal with potential conflicts when calling a method with the same name in multiple parents is called MRO. Basically, if you inherit from multiple parents, the first one in the list is used. To see how it works internally (what is the prioritized order of accessing fields/methods), you can use <code>__mro__</code> field:</p>

<pre class="code"><code>class Parent_A(object):
    some_field = "A"

class Parent_B(object):
    some_field = "B"

class Child(Parent_A, Parent_B):
    pass

print(Child.some_field)
# >>> A
print(Child.__mro__)
# >>> (&lt;class 'Child'>, &lt;class 'Parent_A'>, 
       &lt;class 'Parent_B'>, &lt;class 'object'>)</code></pre>

<p>As you can see in <code>__mro__</code> field, there is the ordered list of instances of how they are called when accessing some field (the first one is always the class itself, then its parents from left, then it goes up in the hierarchy).</p>

<h2>Metaclasses in Python</h2>
<p>Metaclasses are the general concept in object-oriented programming. They allow you to modify the behaviour of your class. Generally speaking, a metaclass is a class whose object is a class (and not just an instance).</p> 

<h3>How to write metaclass</h3>
<p>Metaclass should derive from the type class. It should rewrite one of the methods available in type meta-class (or all of them) - most commonly the <code>__new__</code> method. When a class derives from a specific metaclass, there is a special keyword <code>metaclass</code>. The default metaclass of each class is the type class itself.</p>

<p>Consider the following example that adds a new attribute (containing the number of methods/attributes in class) to all sub-classes and redefine a logic of all methods starting with "some_".</p> 

<pre class="code"><code>class SomeMeta(type):
    def __new__(cls, name, bases, dct):
        # Create instance
        inst = super().__new__(cls, name, bases, dct)
        # Create new method "number_of_elements"
        inst.number_of_elements = len(dct)
        # Filter members starting with "some_"
        all_members = [mt for mt in inst.__dict__ 
                       if mt.startswith("some_")]
        # Replace members starting with "some_" by a method
        for member in all_members:
            setattr(inst, member,
                    # Some method (lambda) 
                    lambda *args: print("OVERLOAD"))
        # Return instance
        return inst


class SomeClass(metaclass=SomeMeta):
    def some_method(self):
        print("some_method")

    def other_method(self):
        print("other_method")


an_inst = SomeClass()
print(an_inst.number_of_elements)
# >>> 4
an_inst.some_method()
# >>> OVERLOAD
an_inst.other_method()
# >>> other_method</code></pre>

<h3>Important methods/variables in a class:</h3>
<p>From the metaclasses perspective, the most important fields and methods are following:</p>
<ul>
    <li><code>__new__</code>: this method is called in the first place when the new class is created. It is an essential method in metaclass when you want to edit class behaviour (typically based on some condition). The return value is a new type.</li>
    <li><code>__dict__</code>: is a dictionary that contains attributes, methods, properties and all other members as keys (keys are the string with the name of entity) and its implementation (or definition) as value. It can be helpful for the selection and modification of some class behaviour.</li>
    <li><code>setattr</code>: a method for setting attributes on some object.</li>
</ul>

<h3>When can be metaclasses helpful</h3>
<p>There are many important use-cases for meta-classes. For example:</p>
<ul>
    <li>Mask some behaviour (typically based on conditions).</li>
    <li>Use class fields to generate a new functionality.</li>
    <li>Conditionally add/remove some attributes (fields, methods).</li>
    <li>Add some testing/debugging code.</li>
    <li>Implement some software design patterns (like singleton).</li>
    <li>Verify the format of class fields and methods.</li>
</ul>
<p>Many frameworks (like Django) use metaclasses internally. For example, Django uses metaclasses for defining database tables from model classes (when doing migrations). Another interesting example is package classutilities (installable using <code>pip install classutilities</code>). This package uses metaclasses to enable class properties (a standard property but on a class level) and to validate configuration classes (restrict fields to upper-case only and remove the possibility of defining constructor).</p>
<h2>Summary</h2>
<p>This article presents many helpful concepts available in the Python language. That includes things like static and class methods, tools for converting dictionary to class object (and vice versa), multiple inheritances, and finally, metaclasses. Metaclasses are a special concept that allows modification of class behaviour. Although it is not a necessary concept in everyday programming, it is essential to know about it (especially for senior engineers).</p>
"""

ENTITY = cr.Article(
    title="More about some useful concepts in the Python language",
    url_alias='more-about-some-useful-concepts-in-the-python-language',
    large_image_path="images/py_advanced_big.jpg",
    small_image_path="images/py_advanced_small.jpg",
    date=datetime.datetime(2021, 2, 13),
    tags=[cr.Tag('Python', 'python'),
          cr.Tag('Design', 'design'),
          cr.Tag('Programming', 'programming'),
          cr.Tag('Performance', 'performance'),
          cr.Tag('Essentials', 'essentials')],
    content=content,
    lead=lead,
    description="Python language has many useful concepts like metaclasses, static or class methods, conversions from dictionary to object instance and other helpful things."  # noqa: E501
)
