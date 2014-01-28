'use strict';

/**
 * Controller for the collection page.
 */
var bdictApp = angular.module('bdictCollection', []);

bdictApp.controller('CorpusListCtrl', function($scope, $http) {

  $http.get('script/gaosengzhuan.json').success(function(data) {
    $scope.docs = data;
  });

});
