# The concept of the universal secure authentification module for gateway
import datetime
import crinita as cr

lead = """One of the everyday challenges in back-end development is how to design and develop a secure gateway. The correctly designed gateway should handle each requirement quickly but concerning security. The security requirement is especially essential concerning the new laws related to GDPR in EU and increasing number of hacking attempts (often successful) to services."""

content = """One of the everyday challenges in back-end development is how to design and develop a secure gateway. The correctly designed gateway should handle each requirement quickly but concerning security. The security requirement is especially essential concerning the new laws related to GDPR in EU and increasing number of hacking attempts (often successful) to services. This article presents a standard way how to deal with this issue and also introduce possible enhancement in performance to this approach. All the content is situated mainly for standard RESTful API gateways.

        <h2>What is a gateway?</h2>
        <p>If we mention gateway here, we technically speaking mean the part that runs some web framework (like Flask, Django). Mostly, when people say a gateway - they are talking about the real application gateway (using technologies like NGNIX). There is though a problem - how to call this entity correctly: it is not a web application (this is the whole system), it is not a web framework (that would be that particular library or technology). That is the reason why the meaning of gateway is somehow inflated here to define this particular entity. So, for this article a gateway = entity that runs a code based build using some web framework (and mainly, implements all routes of the web application).</p>

        <h2>Authentification to the gateway</h2>
        <p>The object of authentification is to allow access only for the eligible users and forbid request of everyone else. </p>
        <p>In a situation when gateway should be available to a broad spectrum of people (typical for mobile/web applications), the only suitable way of authentification is to use standard token-based authentification. Other types (certificated based one and different) are typically not ideal for these purposes (primarily because of troubles with distributing and maintaining certificates for such a vast number of people that significantly reduce the comfort of each user).</p>

        <h2>Token based authentification</h2>
        <p>The logic of the token-based authentification is simple:</p>
        <ol>
            <li>(Sign-Up step) User send the credentials using a secured channel to the server.
            <li>(Verification) Server check the credentials with the stored one (typically in some static RDBMS system).
                <ol>
                    <li>(Send error code) If verification fails, the server returns an error code (in REST API typically 401 or 403 error).</li>
                    <li>(Send the token) If the verification succeeds, the server returns the unique identifier of the session called token. Token has to be saved on both server and client side.</li>
                </ol>
            </li>
            <li>(Request handling) If the user sent some request to the server, it always has to contain the token (session identifier).
                <ol>
                    <li>(Unauthorized) If the server finds out that token is not valid it refuses to handle the request and returns the error code (in RESTful API code 401).</li>
                    <li>(Authorized) If the given token matched to the saved one, the user is considered to be authorized to commit request and the request is handled on the server side. (Be aware of life expectancy of the token)</li>
                </ol>
            </li>
            <li>(Exit) If the user chooses to terminate the session with the server it always should send the request to log-out. This request deletes the token on the server side (without any conditions).</li>
        </ol>
        <p>Any string of bits could technically represent token. Typical representation is some integer or a specific type for the chosen platform. The token must have an only limited life expectancy. If the amount of user's inactivity increases some critical point, the token has to be considered as invalid.</p>

        <h2>Technical implementation in (not only) RESTful API based gateway</h2>
        <p>The authentification process for RESTful API based gateway does not significantly differ from other systems. The specifics are only returned HTTP codes for each request and request to use secured channel for communication (typically with some reliable certificate).</p>

        <h3>Standard implementation</h3>
        <p>The standard implementation uses the SQL server for storing the information about a user (usually login and password in some hashed form). If the Verification step is committed, server receive login and password, compare it to the values in this table. In the case of a match, the log is created. The log is traditionally a row in the independent table that contains information about the user, time of last activity and the token value (represented typically by some string of fixed size). If it comes to the Request handling step, the incoming token is checked (it means selected from log table) and if it exists and the time of the last activity does not breach the rule (life expectancy of the token), the incoming request is handled (and the time of last activity in log table updated).</p>

        <h3>Enhancement of standard implementation</h3>
        <p>Nowadays, the possibility of storing the token and time of last activity is much broader than ever before due to key-value databases. The straightforward way how to improve the performance of the system is to use the key-value database where the key is the value of the token value is the time of last activity. The very user-friendly way how to technically implement this thing is REDIS in-memory database where each item (row) also contains the life-expectancy value in seconds (that makes developers life much easier). </p>
        <p>This solution can mainly increase performance for the extremely overloaded systems (authentification logically the most common request of the gateway). The in-memory database has a significant advantage in low time of access to the values. The enhancement also increases the security of the system because it increases the resistance towards DDoS attacks (due to the logic of the attack, which relies on the limited throughput of the system).</p>
        
        <h2>Ready-made solutions</h2>
        <p>For most of the available languages (and its frameworks for working with RESTful API), there exist some ready-made solution for dealing with authentification. Most of PaaS (Azure, AWS and others) also provides essential services to dealing with this issue. </p>
        <ul>
            <li>PHP (latest version): I can recommend the Laravel framework (https://laravel.com/docs/5.8/authentication)</li>
            <li>Python (latest version): I can recommend a solution in Django framework (https://docs.djangoproject.com/en/2.2/topics/auth/)</li>
            <li>Java, Kotlin (latest version): Use standard way available in Spring Framework.</li>
            <li>C# (ASP.NET): Use standard Token Based Authentification in Web API (standardized sample available online)</li>
        </ul>
        <p>If you prefer the enhanced version of the authentification process, you can modify an existing solution in a part that writes log to the dedicated table, or you can create your solution (which is preferable concerning possible dependencies in ready-made solutions).</p>
        
        <h2>Conclusions</h2>
        <p>The only suitable solution for the broad group of different end-user accessing the gateway is to use token-based authentification. Most of the available (ready-made) solutions follow the standard conception of authentification described above (using token-based authentification related to some SQL relational database). There are also solutions available as external services (without particular description) on all relevant PaaS (AWS, Google Cloud Platform, Azure). The performance of standard (token based) solution can be improved using in-memory key-value database. A very suitable solution for this purposes is REDIS system where each entity (row) can also contain the time value of expiration. The presented enhancement increase both the performance and security of the overall system.</p>
"""

ENTITY = cr.Article(
    title="The concept of the universal secure authentification module for gateway",
    url_alias='the-concept-of-the-universal-secure-authentification-module-for-gateway',
    large_image_path="images/web_big.jpg",
    small_image_path="images/web_small.jpg",
    date=datetime.datetime(2019, 4, 25),
    tags=[cr.Tag('Security', 'security'),
          cr.Tag('Web application', 'web-application'),
          cr.Tag('REST', 'rest'),
          cr.Tag('Design', 'design'),
          cr.Tag('Services', 'services')],
    content=content,
    lead=lead
)
