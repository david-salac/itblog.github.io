# More about some useful concepts in Python language
import datetime
import crinita as cr

lead = """There are many helpful things in Python that are important for effective development. Some of them are less known; some of them are a way more popular. This article presents class methods and static methods (in a Python way), conversion from class to dictionary (and vice versa) and metaclasses and their applications. This article might be helpful for beginners in Python to improve their skills."""

content = """There are many helpful things in Python that are important for effective development. Some of them are less known; some of them are a way more popular. This article presents class methods and static methods (in a Python way), conversion from class to dictionary (and vice versa) and metaclasses and their applications. This article might be helpful for beginners in Python to improve their skills.

<h2>Class and static methods (and fields)</h2>
<p>There are two beneficial concepts in Python language called class and static method. The class method is declared using the following declaration:</p>
<pre class="code"><code>@classmethod
def some_class_method(cls, arg1, arg2...): ...</code></pre>
<p>The first parameter of each class method is the type of class where the method is defined - this differs from the standard method, which takes instance instead (using parameter usually called <code>self</code>). This is helpful either if you want to create some class instance (singleton, for instance) or dealing only with class fields (and not with the class instance).</p>
<p>Very similar concept to a class method is a static method. It differs only slightly:</p>
<pre class="code"><code>@staticmethod
def some_static_method(arg1, arg2): ...</code></pre>
<p>As you can see, there is no <code>cls</code> parameter here. This is the only difference - static method behaves in the same way otherwise. Static methods are not needed very often (since they should not interact with any class field). If there is any interaction with fields, you should prefer to use a class method.</p>

<h2>A bit more about dictionaries and classes</h2>
<p>There can be many good reasons to convert some (class) object to a dictionary (where each field of the object is accessible using logic <code>obj['field']</code>) and vice versa.</p>
<h3>Conversion from dict to class (and) object (using <code>collections.namedtuple</code>)</h3>
<p>A named tuple is a very helpful tool. It basically creates a (sub)class with required fields. It is helpful if you want to have a general type besides the object. Consider the following example (we suppose that dictionary to be converted is variable <code>some_dict</code>):</p>

<pre class="code"><code># Create a type that contains fields equals to keys of the dictionary
SuperType = collections.namedtuple("SomeType", some_dict.keys())
# Create concrete object
obj_from_dict = SuperType(**some_dict)
# Now you can access fields:
obj_from_dict.some_key  # get the value some_dict['some_key']</code></pre>

<p>Conversion from dict to object without class (using <code>types.SimpleNamespace</code>)</p>
<p>This is a much simpler conversion in the case that you do not need a type but just an object:</p>

<pre class="code"><code># Create object:
some_obj = types.SimpleNamespace(**some_dict)
# Now you can access fields:
some_obj.some_key  # get the value some_dict['some_key']</code></pre>

<h3>Conversion of classes to dictionaries</h3>
<p>This is the opposite direction to one presented above. Our ultimate goal is to convert object using logic: <code>some_dict = dict(obj)</code>. The key to success is to define methods <code>__getitem__</code> and <code>keys</code> in the object. Method <code>keys</code> defines which class fields will be serialized to a dictionary. Method <code>__getitem__</code> defines serialization (accessing values using keys). Consider the following example:</p>

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
<p>Python is a language that does not limit number (and type) of classes from which another class can inherit. That allows you to do useful things like writing mixins (that are particularly helpful for unit-test classes), but it can naturally cause some issues. Mainly, if there is some method (or variable) declared in multiple parent classes (having the same name in each parent class).</p> 
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
# >>> (&lt;class 'Child'>, &lt;class 'Parent_A'>, &lt;class 'Parent_B'>, &lt;class 'object'>)</code></pre>

<p>As you can see in <code>__mro__</code> field, there is the ordered list of instances of how they are called when accessing some field (the first one is always the class itself, then its parents from left, then it goes up in the hierarchy).</p>

<h2>Metaclasses in Python</h2>
<p>Metaclasses are the general concept in object-oriented programming. They allow you to modify the behaviour of your class. Generally speaking, a metaclass is a class whose object is a class (and not just an instance).</p> 

<h3>How to write metaclass</h3>
<p>Metaclass should derive from the <code>type</code> class. It should rewrite one of methods (or all of them) <code>__call__</code> or <code>__new__</code> by some custom logic. When class derives from metaclass, there is a special inheritance keyword metaclass.</p>
<p>Consider the following example that adds a new attribute (containing the number of methods/attributes in class) to all sub-classes and redefine a logic of all method starting with "some_".</p> 

<pre class="code"><code>class SomeMeta(type):
    def __new__(cls, name, bases, dct):
        # Create instance
        inst = super().__new__(cls, name, bases, dct)
        # Create new method "number_of_elements"
        inst.number_of_elements = len(dct)
        # Filter members starting with "some_"
        all_members = [mt for mt in inst.__dict__ if mt.startswith("some_")]
        # Replace members starting with "some_" by some method
        for member in all_members:
            setattr(inst, member, lambda *args: print("OVERLOAD"))
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
<ul>
<li><code>__call__</code>: invokes (<code>__new__</code> and <code>__init__</code>). Important when metaclasses operate as software design patterns providers (this method allows you to operate with the instance as if it was a function).</li>
<li><code>__new__</code>: this method is called in the first place when the new instance of a class is created. An essential method for metaclasses when you want to edit class behaviour (typically based on some condition).</li>
<li><code>__dict__</code>: a dictionary that contains attributes, methods, properties and all other members as keys (keys are the string with name) and its implementation (or definition) as value. Can be helpful for the selection and modification of some class behaviour.</li>
<li><code>setattr</code>: a method for setting attributes on some object</li>
<li><code>type</code>: the <code>type</code> is the metaclass of which classes are instances.</li>
</ul>

<h3>When can be metaclasses helpful:</h3>
<ul>
<li>mask some behaviour (typically based on conditions)</li>
<li>conditionally add/remove some attributes (fields, methods)</li>
<li>add some testing/debugging code</li>
<li>implement some software design patterns (like singleton)</li>
</ul>
"""

ENTITY = cr.Article(
    title="More about some useful concepts in Python language",
    url_alias='more-about-some-useful-concepts-in-python-language',
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
