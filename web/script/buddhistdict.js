// Angular code for main search page
var textApp = angular.module('textApp', ['ngSanitize']).
  filter('processNotes', function() {
    return function(input) {
      var re = /Sanskrit:([^,])/;
      if (re.test(input)) {
        return input.replace(re, "SANSKRIT: <a href='#'>$1</a>");
      }
      return input;
    }
  });

textApp.controller('textCtrl', function($scope, $http, $sce) {
  var self = this;
  $scope.formData = {};
  $scope.formData.langtype = 'literary';
  $scope.results = {};
  $scope.submit = function() {
    var re = /[\u0041-\u007F\u0080-\u00FF\u0100-\u017F\u0180-\u024F\u0300-\u036F]/;
    var englishSearch = re.exec($scope.formData.text);  
    var url = "textlookup.php";
    if (englishSearch) {
      url = "englishsearch.php"; 
    }
    $http({url: url, 
           method: 'post', 
           data: $.param($scope.formData),
           headers : {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
    }).success(function(data) {
      $("#lookup-help-block").hide();
      $scope.results = data;
      if ($scope.results.words) {
        for (var word in $scope.results.words) {
          if (word.notes) {
            self.explicitlyTrustedHtml = word.notes;
          }
        }
      }
    }).error(function(data, status, headers, config) {
      $("#lookup-help-block").hide();
      $scope.results = {"error": data};
    });
  };
});

