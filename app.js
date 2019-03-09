var app = angular.module('app', []);

app.controller('MainController', function ($scope, $http){
   $http({
      method: 'GET',
      url: 'https://api.myjson.com/bins/xt2h6'
   }).then(function (response){
     $scope.data = response.data;
     console.log($scope.data);
   },function (error){
     console.log(console.error);
   });

   $scope.streetnumber;
   $scope.streetname = "";
   $scope.city = "";
   $scope.province = "";
   $scope.reload = $route.reload();
}
);
