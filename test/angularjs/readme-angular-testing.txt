Angular Testing Readme 
===============================================================================

1. Install Node.js (http://nodejs.org)
2. Install the karma plug-in

  $ sudo npm install karma

3. Download the Angular JS library and put it at $PROJECT_HOME/web/script/angular.min.js.
4. Start Node.js as a static file HTTP server.

  $ cd $PROJECT_HOME/test
  $ node test/angularjs/script/web-server.js

5. Test the web pages out at 
  http://localhost:8000/web/index.html
