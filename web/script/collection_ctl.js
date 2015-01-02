'use strict';

/**
 * Controller for the collection page.
 */
var bdictApp = angular.module('bdictCollection', [], function($locationProvider) {
    $locationProvider.html5Mode(false);
    $locationProvider.hashPrefix('!');
  });

bdictApp.controller('CorpusListCtrl', function($scope, $http, $location) {

  //console.log("collection_ctl.js $location.url() = " + $location.url())
  var colnameElem = document.getElementById("colname")
  if (colnameElem) {
    var colname = colnameElem.value;
  } else if ($location.url().indexOf("/") > -1) {
    //console.log("collection_ctl.js $location.path() = " + $location.path())
    colname = $location.path().substring(1);
  } else {
    //console.log("collection_ctl.js colname is not defined.")
    colname = "corpus_all";
  }

  var collection = "script/corpus_all.json"
  if (colname == 'corpus_all') {
    $scope.main_doc = {'source_name': 'Whole Collection'};
    $scope.docs = {};
  } else {
    collection = "script/" + colname + ".json";
    //console.log("collection_ctl.js collection: " + collection + ", colname = " + colname)

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
