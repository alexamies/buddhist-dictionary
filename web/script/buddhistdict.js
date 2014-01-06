// Angular code for main search page
var textApp = angular.module('textApp', []);
textApp.controller('textCtrl', function($scope, $http) {
  $scope.formData = {};
  $scope.results = {};
  $scope.submit = function() {
    var re = /[\u0021-\u007F\u0080-\u00FF\u0100-\u017F\u0180-\u024F\u0300-\u036F]/;
    var englishSearch = re.exec($scope.formData.text);  
    var url = "textlookup.php";
    if (englishSearch) {
      alert('English search');
      url = "englishsearch.php"; 
    }
    $http({url: url, 
           method: 'post', 
           data: $.param($scope.formData),
           headers : {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
    }).success(function(data) {
      $("#lookup-help-block").hide();
      $scope.results = data;
    }).error(function(data, status, headers, config) {
      alert('Error: ' + data);
    });
  };
});
