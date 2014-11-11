'use strict';



weddingApp.controller('GuestPartyCtrl', function ($scope, $http)
{
    $http.get('/parties').success(function (data)
    {
        console.log(data);
        $scope.parties = data;
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