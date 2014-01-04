// Angular code
var textApp = angular.module('textApp', []);
textApp.controller('textCtrl', function($scope, $http) {
  $scope.formData = {};
  $scope.results = {};
  $scope.submit = function() {
    $http({url: 'textlookup.php', 
           method: 'post', 
           data: $.param($scope.formData),
           headers : {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
    }).success(function(data) {
      $scope.results = data;
    }).error(function(data, status, headers, config) {
      alert('Error: ' + data);
    });
  };
});
