'use strict';

/**
 * Controller for the collection page.
 */
var bdictApp = angular.module('bdictCollection', [], function($locationProvider) {
    $locationProvider.html5Mode(false);
    $locationProvider.hashPrefix('!');
  });

bdictApp.controller('CorpusListCtrl', function($scope, $http, $location) {

  var colname = "corpus_all"
  var collection = "script/corpus_all.json"
  if ($location.path() == '') {
    $scope.main_doc = {'source_name': 'Whole Collection'};
    $scope.docs = {};
  } else {
    colname = $location.path().substring(1);
    collection = "script" + $location.path() + ".json";
    console.log("path = " + $location.path() + ", collection: " + collection + ", colname = " + colname)

    $http.get("script/corpus.json").success(function(data) {
      for (var i = 0; i < data.length; i++) {
        var doc = data[i];
        if (("uri" in doc) && (doc.uri == colname)) {
          $scope.main_doc = doc;
        }
      }
    });
  }

  $http.get(collection).success(function(data) {
    $scope.docs = data;
  });

});
