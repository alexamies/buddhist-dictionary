'use strict';

/**
 * Controller for the collection page.
 */
var bdictApp = angular.module('bdictCollection', []);

bdictApp.controller('CorpusListCtrl', function($scope, $http, $location) {

  var collection = "script" + $location.path() + ".json";

  $http.get(collection).success(function(data) {
    $scope.docs = data;
  });

});
