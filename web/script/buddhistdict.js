// Angular code
var textSearchApp = angular.module('textSearchApp', []);
textSearchApp.controller('textSearchCtrl', function($scope, $http) {
  $scope.formData = {};
  $scope.results = {};
  $scope.submit = function() {
    $http({url: 'textlooup.php', 
           method: 'post', 
           data: $.param($scope.formData),
           headers : {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
    }).success(function(data) {
                              $scope.results = data;
                              });
  };
});
