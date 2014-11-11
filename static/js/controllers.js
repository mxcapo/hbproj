'use strict';

var weddingAppControllers = angular.module('weddingAppControllers', []);

weddingApp.controller('PartyListCtrl', function ($scope, $http)
{
    $http.get('/view/parties').success(function (data)
    {
        console.log(data);
        $scope.parties = data;
        console.log(data);
    }).error(function (data)
    {
        console.log("try again");
    });

    $scope.orderProp = "side";
    
});


// weddingApp.directive('partyCard', function ($http) {
//     function link(scope, element) {
//         console.log("okie doek");
//         $http.get('/parties').success(function (data){
//         console.log(data);
//         }).error(function(data){
//         console.log(data);
//     });

//     }
//     return {
//         restrict: "A",
//         link: link,
//         template: ''
//     };
// });