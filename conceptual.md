### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

there are slight changes in syntax between the two of them. Python is object oriented while JS is scripting. Python has mutable and immutable information
with specific methods for each. python also allows for comparison of dictionaries and lists while JS does not

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

<!-- dict.get('c') or dict.get('key') -->

- What is a unit test?

  <!-- a way of testing individual components in a simple way -->

- What is an integration test?

  <!-- testing that the components of the code work together -->

- What is the role of web application framework, like Flask?

<!-- to decide which requests to respond to and how to respond to them -->

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  
  <!-- If i am describing something then i may use query param because the user is describing what they are looking for but if i just need to route them to the correct pages then i would go with route url
  routes can also be better if  the webpage is going to have many redirects or multiple options before an end point. if we dont use routes in this situation the url query will become very long  vs a few routes stacked together -->

- How do you collect data from a URL placeholder parameter using Flask?

<!-- by specifying a variable in app.route then passing it as a parameter in the function
@app.route('/leg/<turkey>')
def food(turkey): -->


- How do you collect data from the query string using Flask?

 <!-- by using request.args so flask can make key value pairs from what is in the url
 usually shown by ?key=value -->

- How do you collect data from the body of the request using Flask?

<!-- by using request.form -->

- What is a cookie and what kinds of things are they commonly used for?

<!-- they are small bits of information that are stored in the browser
and they are a way to make http stateful -->

- What is the session object in Flask?

<!-- an upgrade on cookies that allow for more security in the sense that the client side cant change them without knowing the secret key. This allows the browser to remember things without having to create more cookies on the client side. -->

- What does Flask's `jsonify()` do?

<!-- serialize data to JSON format -->