# The concepts for the secure authentication process in web application
import datetime
import crinita as cr

lead = """One of the everyday challenges in back-end development is designing and developing a secure authentication and authorization process. There are many solutions available, but deploying them without a thorough understanding of how they internally work is dangerous. Therefore, we present here the most common way of dealing with the authentication process. The most popular forms of dealing with this issue are session-based authentication and token-based authentication."""

content = """<p class="lead">One of the everyday challenges in back-end development is designing and developing a secure authentication and authorization process. There are many solutions available, but deploying them without a thorough understanding of how they internally work is dangerous. Therefore, we present here the most common way of dealing with the authentication process. The most popular forms of dealing with this issue are session-based authentication and token-based authentication.</p>

<h2>What are authentication and authorization?</h2>
<p>Authentication is a process where an entity (user or any other client, like embedded device) provides its credential and another entity (typically a server) verifies these credentials. The outcome of authentication is to determine whether an entity trying to authenticate is really the user. So technically, it is a yes/no answer. If the answer is no, you typically see something like provided credentials are incorrect. If the answer is yes, the next step usually is the authorization of the request. Authentication is always performed when you log into your email, access your internet banking, or log into your locked laptop.</p>
<p>Authorization is a process when an application (server) decides if the already authenticated user has sufficient credentials to perform given action. It is a separate step performed after authentication. If the authorization process files, the response is typically forbidden (HTTP returns code 403). In each system generally are many rings of users - some have more privileges than others. Typically, some tasks (like accessing the user's profile) are dedicated to a specific user (and forbidden for any other user), which is called Object Level Permission (OLP). Management of OLP is a critical system feature related to authorization. Authorization is, for example, performed if you try to delete a post in some discussion (only the author of the post and administrator are usually entitled to do so) - here, you need to have the delete permission on a given object (from the OLP point of view). Another example is from a shared computer - you cannot access other users' files (unless you are a system administrator).</p>
<h2>Where technically is the authentication process located?</h2>
<p>When you access any route in your web application, you technically send an HTTP request which has defined composition. Each request contains its header, which is the place where are authentication information located. The header should contain keys and values pairs representing metadata of request. The key (or keys) related to authentication depends on the technology you use; most commonly, it is just 'Authorization'. The value also depends on technology, but most commonly, it starts with one of the following: ' Bearer', 'Token', 'Basic', 'X-API-Session', 'X-Session' or others. </p>
<p>The web service's dedicated part (or parts) then takes this information (value in the header assigned to the specific key dedicated do authentication) and checks its validity. Where and how depends explicitly on chosen technology and configuration. Sometimes, it is the gateway's work (NGIX can validate JWT tokens and refuse connection with the invalid token), or it can be the application itself (validate header and check if it matches some entity in a database, this is usually a part of view or route definition). Often, many entities need to interact to process authentication requests (typically in the case of 0Auth when you interact with an external provider).</p>
<h2>Fundamental authentication principles</h2>
<p>The following principles are the most common way to deal with authentication:</p>
<ol>
    <li>Token-based authentication</li>
    <li>Session-based authentication</li>
    <li>Basic authentication</li>
</ol>
<p>Each of these ways has its pros and cons. Also, most web frameworks (like Django) supports all these ways. It is necessary to be aware of how they internally work - as the proper selection (and configuration) has a massive impact on security.</p>
<h3>Basic authentication</h3>
<p>Represents the most straightforward way of the authentication process (and one of the oldest). The header of the request contains the following:</p>
<pre class="code"><code>Authorization: Basic CREDENTIALS_BASE_64></code></pre>
<p>where <code>CREDENTIALS_BASE_64</code> is the Base64 encoding of login (ID) and password merged by colon character.</p>
<p>You can immediately see the security vulnerabilities of this process. If you use a connection that is not encrypted (plain, no SSL), then everybody can read your credentials. This makes basic authentication suitable only for local development or particular applications (say, protected inside VPN).</p>
<h3>Session-based authentication</h3>
<p>As the name suggests, it is based on sessions that are typically represented by cookies. The protocol usually follows the following logic:</p>
<ol>
<li>User (front-end) sends credentials to a server.</li>
<li>The server starts a session and returns the session ID.</li>
<li>User (front-end) stores session ID in the cookie.</li>
<li>Cookie with the session ID is sent with every request to a server.</li>
<li>The server validates session ID with its internal database and decides whether to authorize the request.</li>
</ol>
<p>The described principle is technically the combination of session-based authentication and token-based one. You can also store your credentials in your cookies and send them (then it is a combination with basic authentication - which is not secure). The underpinning principle is the session represented by cookies (either permanent or dedicated to a specific session). </p>
<p>Some technologies do not use cookies but send the session ID in the request header - but that is technically the equivalent to token-based authentication. In the worst case, the session ID can also be added to the URL (which is exceptionally unsecured).</p>
<h3>Token-based authentication</h3>
<p>As the name suggests, the main component of token-based authentication is a token. The principle is as follows:</p>
<ol>
<li>User (front-end) sends credentials to a server.</li>
<li>The server creates an (optimally secure) token and returns it.</li>
<li>User (front-end) stores this token as a local variable.</li>
<li>Token value is sent to a server (in the header) with every request.</li>
<li>The server validates token ID with its internal database and decides whether to authorize the request.</li>
<li>Optionally: server updates the value of the token (to keep communication secure).</li>
</ol>
<p>As you can see, the main difference with session-based authentication (based on session ID) is how the token is saved and sent to a server. In the optimal case, the token is recreated with every request (and the new value returned) - so the user (front-end) does not have to store it in any variable - this is, however, not required.</p>
        
<h2>Implementation</h2>
<p>The quality of implementation significantly differs from framework to framework. The most popular open-source framework Django (and mainly RestFramework for Django), support all three ways. The technical quality of token-based authentication is, however, inferior. By default, an assigned token is valid permanently - that has many security consequences. It is, therefore, crucial to always check the quality of implementation (if possible) manually. It is a huge advantage to use open-source components (where you can verify things manually). The simple fix for Django is to use the Simple JWT extension, which implements JSON Web Token authentication logic. The quality of this extension is significantly higher than the default DRF version.</p>
<h3>OAuth protocol (and similar protocols)</h3>
<p>OAuth is technically a ready-made open-source solution for authentication and authorization, published in 2010. It is beneficial in the case of multiple services requiring authentication (and sharing resources) as the entire logic is in one place (single sign-on logic). Internally, OAuth works as a token-based authentication (with JWT tokens). It uses a third party to perform authentication (validate credentials) and authorization for the (new) service. Once you authorize a new service on the third-party site, it works as a standard token-based authentication. For example, you can find OAuth if you want to log in to some service that offers you to use your Facebook, Apple or Google account to sign in (usually, there is a window that contains a button: use your Facebook account or similar).</p>
<p>Many other services also provide single sign-on logic similar to OAuth. The popular option is OpenID - it internally works on similar logic - however, you do not need to authorize a new service (implicit). So the main logic of OpenID is really to authenticate a user (not to authorize a new service). SAML is another option similar to OAuth - it uses a similar logic (but a bit less user-friendly).</p>
<h3>Two-factor authentication and multi-factor authentication (MFA)</h3>
<p>Another popular option in the world of authentication is multi-factor authentication (MFA), typically two-factor. Technically, the authentication process is split into two (or multiple) parts. The first part is to provide credentials to the authentication server. The next part usually uses some third entity to generate a random secure key sent to a user by some separated channel (using SMS, a mobile application or some specialized hardware). Only if both credentials and secure key match, the authentication process can continue. This process makes the situation safer because there is a higher probability that a user is really a concrete person - it is much harder to hack all channels than to steal credentials (login and password).</p>

<h3>Typical authentication logic</h3>
<p>The authentication process usually follows the logic depicted on the schema below:</p>
<figure>
    <img src="images/auth_schema.png" alt="Schema of authentication logic with standard components">
    <figcaption>Figure 1: Schema of authentication logic with standard components</figcaption>
</figure>
<p>As you can see, the authentication module (or service) is logically independent of the rest of the application - which is the most common logic (and the most secure one). Internally it verifies user credentials in a database and generates a token (stored in a database, usually in-memory cache). Then, the application accepts the request with the token, verifies it using the Authentication component, and serves response (either forbidden error or actual response).</p>

<h2>Conclusions</h2>
<p>The most common technical ways for dealing with authentication of web-application are presented. These are basic authentication, session-based authentication and token-based authentication. Each of these logic has its pros and cons (and some of them are not mutually exclusive). Generally, the most secure is token-based authentication. Also, the most common third-party implementations are presented - mainly OAuth - these services are helpful for the implementation of single sign-on logic (user uses just one credential for multiple services). The multi-factor authentication concept is then presented to improve application security by using numerous verification channels.</p>
"""

ENTITY = cr.Article(
    title="The concepts for the secure authentication process in web application",
    url_alias='the-concepts-for-the-secure-authentication-process-in-web-application',
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
