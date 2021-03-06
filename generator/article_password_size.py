# What is really the optimal size and composition of the password
import datetime
import crinita as cr

lead = """During the last few years, we could see a revolution if it comes to entering passwords to online services (e-shops, email providers, social networks etc.). This revolution ensued in a surge of the forgotten passwords. More and more users forget password just after entering it. This leads to an increasing number of the toolkits for storing passwords where each has its own vulnerabilities."""

content = """During the last few years, we could see a revolution if it comes to entering passwords to online services (e-shops, email providers, social networks etc.). This revolution ensued in a surge of the forgotten passwords. More and more users forget password just after entering it. This leads to an increasing number of the toolkits for storing passwords where each has its own vulnerabilities. But what is actually a reality of password security in a mathematical point of view? Does using of each special character have any impact on security? How should the real secure password look like? There exist surprisingly simple and precise answers for all of these questions, let's take a look.

        <h2>Cryptographic hash function</h2>
        <p>After you enter the password during registration on some site it is typically sent to the server in so-called plain text form (plain text means that it is sent as it is, without any irreversible modification). If there is no security issue on server side (which is not always true), the server does not store the password in a plain text form due to security (consider that someone could hack the database and has all the available passwords). Instead of this the hash of the password is computed and stored (this process is often more difficult due to salting of password and other processes). The has is computed using the cryptographic hash function. There is a lot of hash function which each has its pros and cons (in a security point of view). The most popular hash functions in nowadays are members of families called SHA-1 and SHA-2 and the specific hash function called MD5. </p>

        <p>The logic of the hash function is that if you have an input value, you can very quickly compute the output value (the hash). But if you have the output you cannot quickly compute the matching input. Optimally you have to try each possible combination of the input to receive desired output. And this operation costs a lot of time (so much that you cannot imagine, typically like billions of billions of years and so on if you have a very powerful computer). </p>

        <h3>Intermezzo: something about bites, bytes, numbers and ASCII</h3>
        <p>You have probably heard that everything in computer science is about bites and bytes. So what is that a bit? It simply a number. But instead of our numbers that have values from 0 to 9, a bit can have only values from 0 to 1. And byte is simply a number that has just 8 bites. </p>

        <p>Similarly, as you can play with decimal numbers, you can play with bites. You can add them, subtract them etc. What is most important in our situation is the following: consider that you have a number composed of N bites. For example, N could be 8, 16, 48574 or any other natural number. Question is how many possible combinations there are in this string of N bites? For example, if N is 8, the combination could be 00000000, 00001001, 00000001 and so on. You can simply write each possible combination and count them or you can use the following trick. Consider that you have 3 digit decimal number then you can quickly say that it can have 1000 combinations. How could you quickly compute it? Simply by computing 10 power to 3, where 10 is the root of our numerical system (decimal = 10). In our example, we have just 2 possible values (binary system). So answer to our question is that we have 2 power to N combinations. In our example 2 power to 8 equals to 256 combinations. </p>

        <p>So far so good. But can I also compute how many bits do I need if knowing number of possible combinations (inverse task)? Yes, you can, quite simply using logarithm function. More precisely logarithm function base 2 (binary). There are a lot of online calculators for computing such value. This function is especially important later in this article so please take care you understand it. It practically returns some decimal number for almost all values, so practically you have to round it up if you really want to know how many bits you need to reserve.</p>

        <p>Well, but how can I transform normal characters, such as latter A to a number (or sequence of bites)? The answer is the ASCII table. ASCII table is a simple encoding table. On the beginning of computers, there had to be a unified way of how to encode each character to a particular string of bites (number in binary form) and vice versa. ASCII table contains the pairs of characters and a matching string of 8 bites (1 byte) that represent this character. There are 256 characters represents in ASCII table. If you need some special characters (symbols in Hebrew, for example), there exist successors of this table (for example UTF-8, Unicode and others). </p>


        <h2>Why did I say all of this? Because of the Digest size.</h2>
        <p>As mentioned above the hash functions differs in many ways. One of the fundamental parameters of each hash function is called digest size. It is simply a number of bites that are the output of each particular hash function. Following table depicts digest sizes of the most popular hash functions:</p>

        <table>
            <tr>
                <th style="padding-right: 20px;">Hash function</th><th style="padding-right: 20px;">Variant</th><th style="padding-right: 20px;">Digest size</th>
            </tr>
            <tr>
                <td>MD5</td>
                <td>-</td>
                <td>128</td>
            </tr>
            <tr>
                <td>SHA-1</td>
                <td>-</td>
                <td>160</td>
            </tr>
            <tr>
                <td>SHA-2</td>
                <td>224</td>
                <td>224</td>
            </tr>
            <tr>
                <td>SHA-2</td>
                <td>256</td>
                <td>256</td>
            </tr>
            <tr>
                <td>SHA-2</td>
                <td>384</td>
                <td>384</td>
            </tr>
            <tr>
                <td>SHA-2</td>
                <td>512</td>
                <td>512</td>
            </tr>
        </table>
        

        <p>The logic is that if the input has more bites that the current digest size of the hash function, the security of the system does not increase. It same like when you resize a picture to some smaller size and than try to resize it back again. You always have a blurred image, because you lose some data. So it is meant to target to just as many bites of input as the digest size of the used hash function is or slightly more if necessary due to rounding. </p>

        <p>To compute what is the optimal size of the input let me introduce the following:</p>
        <ul>
            <li>There are 26 letters in the alphabet. If we count uppercase and lowercase letters separately, it is 52 letters at all.</li>
            <li>There is 10 decimal digit. It means 10 possible combinations for each character (0,1 and so on up to 9).</li>
        </ul>
        <p>If we are constructing password we should be aware that it is just a string of characters. Each character could some limited number of accepted values:</p>
        <ul>
            <li>If we choose just password with numbers, each character can possibly have 10 combinations.</li>
            <li>If we choose just password with lowercase latter, each character can possibly have 26 combinations.</li>
            <li>If we add uppercase latter, each character can possibly have 52 combinations.</li>
            <li>If we add numbers, each character can possibly have 62 combinations.</li>
            <li>If we add some special characters (typically we can easily write just about 10 special characters on keyboard), we have 72 combinations.</li>
        </ul>
        <p>So what can we say about a secure password so far? Let&#8217;s go back to our base-2 logarithm. We now know how many combinations each character can have (based on how complex password we have chosen). But how many bits could represent these numbers? The answer is the base-2 logarithm of each value:</p>
        <table>
            <tr>
                <th style="padding-right: 20px;">N</th><th style="padding-right: 20px;">bit size = log<sub>2</sub> (N)</th>
            </tr>
            <tr>
                <td>10</td>
                <td>3.3219</td>
            </tr>
            <tr>
                <td>26</td>
                <td>4.7004</td>
            </tr>
            <tr>
                <td>52</td>
                <td>5.7004</td>
            </tr>
            <tr>
                <td>62</td>
                <td>5.9541</td>
            </tr>
            <tr>
                <td>72</td>
                <td>6.1699</td>
            </tr>
        </table>

        <p>So we know what is the bit size of each password combination (you can check it using online calculator). We know what is the desired size of the input (which is equal to the digest size). So the answer to optimal password length is simple, just divide digest size by bit size of each character (in the table) and round it up! It is really so simple. If you choose a password that is bigger than the value you have computed this way than it is useless.</p>

        <h2>What is the optimal size of the password</h2>
        <p>Based on the logic described above I have computed a simple table for you.</p>
        <table>
            <tr>
                <th style="padding-right: 20px; width: 30%;">Digest size</th>
                <th style="padding-right: 20px;">128</th>
                <th style="padding-right: 20px;">160</th>
                <th style="padding-right: 20px;">224</th>
                <th style="padding-right: 20px;">256</th>
                <th style="padding-right: 20px;">384</th>
                <th style="padding-right: 20px;">512</th>
            </tr>
            <tr>
                <td style="padding-right: 20px;">Password length for numeric only</td>
                <td>39</td>
                <td>49</td>
                <td>68</td>
                <td>78</td>
                <td>116</td>
                <td>155</td>
            </tr>
            <tr>
                <td style="padding-right: 20px;">Password length for lowercase only</td>
                <td>28</td>
                <td>35</td>
                <td>48</td>
                <td>55</td>
                <td>82</td>
                <td>109</td>
            </tr>
            <tr>
                <td style="padding-right: 20px;">Password length for lowercase and uppercase</td>
                <td>23</td>
                <td>29</td>
                <td>40</td>
                <td>45</td>
                <td>68</td>
                <td>90</td>
            </tr>
            <tr>
                <td style="padding-right: 20px;">Password length for lowercase, uppercase and numeric</td>
                <td>22</td>
                <td>27</td>
                <td>38</td>
                <td>43</td>
                <td>65</td>
                <td>86</td>
            </tr>
            <tr>
                <td style="padding-right: 20px;">Password length for lowercase, uppercase, numeric and special characters</td>
                <td>21</td>
                <td>26</td>
                <td>37</td>
                <td>42</td>
                <td>63</td>
                <td>83</td>
            </tr>
        </table>

        <p>That is a really lovely table, isn&#8217;t it? But what does it actually say is really important:</p>
        <ul>
            <li>It is not meaningful to use a special character in a password (it very difficult to remember them and write them to foreign layouts).</li>
            <li>The sufficiently secure password to each application is 22 alphanumeric random character.</li>
        </ul>
        <p>The second sentence requires some explanation because it partially contradicts to the overall logic. So far we know, our current computers are not capable to compute more than one billion of the complex operations per second. There is no known technology that could increase this performance exponentially to this value. It seems to be like an extremely huge number, but it actually is not. Consider how many possible combinations does 128 bits number has? It is exactly  340,282,366,920,938,000,000,000,000,000,000,000,000. The number that has 39 decimal digits. Consider that we use all available computers in a world to find correct input value. We have roughly about 10 billions computers, each can compute a billion combinations per second (reality is, that computer is much slower, but we can ignore it now). In that case, it would take 10 power to 19 seconds to find the correct value which is more than 100,000,000,000 years. I think that you do not have to be worried that someone hack your password after such a long time.</p>

        <p>Of course, it is critically important to mention that you have to use a really random password. A random set of characters and numbers. For example: Sz2xNgVaRmQJrkL0eEAI8H, definitely not passwords like: JoHnOhMGoDItIs2So1CooL. Be aware of this. Believe yourself and learn one meaningfully large password! If you can, you can as well use an only alphabetical password with lower and upper cases of size 23 characters. Each is equally secure.</p>

        <h2>Conclusions</h2>
        <p>The main conclusion of this article is that it is not so important whether special characters are included in your password or not. It is also not so important whether numbers are included or not. The password which is secure enough is 23 random alphabetical characters (lower and upper case). On the critically important is the size of the password. Everything which has less character than 22 alphanumerical characters (or 23 alphabetical lower/upper case) can be considered as vulnerable. </p>
"""

ENTITY = cr.Article(
    title="What is really the optimal size and composition of the password",
    url_alias='what-is-really-the-optimal-size-and-composition-of-the-password',
    large_image_path="images/password_big.jpg",
    small_image_path="images/password_small.jpg",
    date=datetime.datetime(2018, 11, 15),
    tags=[cr.Tag('Security', 'security'),
          cr.Tag('Web application', 'web-application'),
          cr.Tag('Password', 'password'),
          cr.Tag('Design', 'design'),
          cr.Tag('Cryptosystem', 'cryptosystem')],
    content=content,
    lead=lead
)
