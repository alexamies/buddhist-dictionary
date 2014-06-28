// Angular code for main search page
var textApp = angular.module('sanskritQueryApp', ['ngSanitize']);

textApp.controller('sanskritQueryCtrl', function($scope, $http, $sce) {
  $scope.formData = {};
  $scope.formData.matchtype = 'approximate';
  $scope.results = {};
  $scope.submit = function() {
    $scope.results = {"msg": "Searching"};
    var url = "sanskrit_ajax_search.php";
    $http({url: url, 
           method: 'post', 
           data: $.param($scope.formData),
           headers : {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
    }).success(function(data) {
      $("#lookup-help-block").hide();
      $scope.results = data;
      //alert($scope.results.words)
      if ($scope.results.words && $scope.results.words.length > 0) {
        for (var i=0; i < $scope.results.words.length; i++) {
          word = $scope.results.words[i];
        }
        delete $scope.results.msg;
      } else {
          $scope.results = {"msg": "No results found"};
      }
    }).error(function(data, status, headers, config) {
      $("#lookup-help-block").hide();
      $scope.results = {"msg": data};
    });
  };
});

