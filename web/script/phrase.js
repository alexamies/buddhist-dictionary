// Angular code for main search page
var phraseApp = angular.module('phraseApp', []);
phraseApp.controller('phraseCtrl', function($scope, $http) {
  var url = "phraselookup.php?id=" + id;
  $http({url: url, method: 'get'
  }).success(function(data) {
    $scope.results = data;
  }).error(function(data) {
    alert('Error: ' + data);
  });
});
