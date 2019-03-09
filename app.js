var app = angular.module('app', []);

function download(text, name, type) {
  var a = document.getElementById("a");
  var string = document.getElementById('streetNumber') + document.getElementById('streetName') + document.getElementById('City') + document.getElementById('Province');
  var message = document.getElementById('message');
  var file = new Blob([text], {type: type});
  a.href = URL.createObjectURL(file);
  a.download = name;
}


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
   $scope.tempaddress = "hi";

   $scope.address = function(){
     $scope.streetname = $scope.streetname.replace(' ', '+');
     return $scope.streetnumber.toString() + '+' + $scope.streetname + '+' + $scope.city + '+' + $scope.province;
   }

   $scope.reviewProgram = "";
   $scope.reviewDescript = "";

}
);

// $("#save-btn").click(function(){
//   var string = document.getElementById('streetNumber') + document.getElementById('streetName') + document.getElementById('City') + document.getElementById('Province');
//   var message = document.getElementById('message');
//   console.log(string + "\n" + message);
//   var blobl = new Blob([string + "\n" + message], {type: "text/plain;charset-utf-8"});
//   saveAs(blobl, "user-input.txt");
// });
