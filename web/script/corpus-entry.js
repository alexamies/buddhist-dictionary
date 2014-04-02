'use strict';
/* Angular app for managing corpus text entries */

/* App Module */
var corpusEntryApp = angular.module('corpusEntryApp', [
  'ngRoute',
  'corpusEntryControllers'
]);

corpusEntryApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('', {
        templateUrl: 'corpus.html'
      }).
      when('/:entryId', {
        templateUrl:  function($routeParams) {
          return 'corpus/gloss/' + $routeParams.entryId;
        }
      }).
      otherwise({
        redirectTo: ''
      });
  }]);

/* Controller */
var corpusEntryControllers = angular.module('corpusEntryControllers', []);

corpusEntryControllers.controller('corpusEntryCtrl', function ($scope) {
  $scope.loadingText = 'Loading ...';
  $scope.setLoadingText = function(loadingText) {
      $scope.loadingText = loadingText;
  }
});
