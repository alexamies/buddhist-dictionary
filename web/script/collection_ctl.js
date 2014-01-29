'use strict';

/**
 * Controller for the collection page.
 */
var bdictApp = angular.module('bdictCollection', []);

bdictApp.controller('CorpusListCtrl', function($scope, $http, $location) {

  var colname = $location.path().substring(1);
  var collection = "script" + $location.path() + ".json";

  $http.get("script/corpus.json").success(function(data) {
    for (var i = 0; i < data.length; i++) {
      var doc = data[i];
      if (("uri" in doc) && (doc.uri == colname)) {
        $scope.main_doc = doc;
      }
    }
  });

  $http.get(collection).success(function(data) {
    $scope.docs = data;
  });

});
