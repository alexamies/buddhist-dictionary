// Angular code for main search page
var textApp = angular.module('textApp', ['ngSanitize']);

textApp.controller('textCtrl', function($scope, $http, $sce) {
  var re = /[^\u0040-\u007F\u0080-\u00FF\u0100-\u017F\u0180-\u024F\u0300-\u036F]/;
  $scope.formData = {};
  $scope.formData.langtype = 'literary';
  $scope.formData.matchtype = 'approximate';
  $scope.results = {};
  $scope.submit = function() {
    $scope.results = {"msg": "Searching"};
    var hasCJK = re.exec($scope.formData.text);  
    var url = "englishsearch.php";
    if (hasCJK && ($scope.formData.matchtype == 'approximate')) {
      url = "textlookup.php";
    }
    $http({url: url, 
           method: 'post', 
           data: $.param($scope.formData),
           headers : {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
    }).success(function(data) {
      $("#lookup-help-block").hide();
      $scope.results = data;
      var sans_re = /Sanskrit:[\s]+([^,]*)(.*)/;
      if ($scope.results.words && $scope.results.words.length > 0) {
        for (var i=0; i < $scope.results.words.length; i++) {
          word = $scope.results.words[i];
          if (word.notes) {
            if (sans_re.test(word.notes)) {
              word.notes =  word.notes.replace(sans_re, "Sanskrit: <a href='sanskrit_query.php?word=$1'>$1</a> $2");
            }
            self.explicitlyTrustedHtml = word.notes
          }
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

