'use strict';

var weddingAppControllers = angular.module('weddingAppControllers', 
    ['ngRoute']);

weddingApp.controller('PartyListCtrl', function ($scope, $http)
{
    $http.get('/view/parties').success(function (data)
    {
        // console.log(data);
        $scope.parties = data;
        // console.log(data);
    }).error(function (data)
    {
        console.log("try again");
    });

    $scope.orderProp = "side";

});

weddingApp.controller('FilterCtrl', function ($scope, $http)
    {
        $http.get('/groupings').success(function (data)
        {
            console.log(data);
            $scope.groupings = data;
        });

        $scope.filter = {};

        $scope.getOptionsFor = function (propName)
        {
            // console.log(propName);
            var list = $scope.groupings[propName];
            // console.log(list);
            return ($scope.groupings[propName] || [])
            // .map(function (p)
            // {
            //     console.log(p["ok"]);
            //     console.log(p[propName]);
            //     console.log(p);
            // });
            .filter(function (p, idx, arr)
            {
                return arr.indexOf(p) === idx;
            });
        };
        $scope.filterByProperties = function (party)
        {
            var matchesAND = true;
            for (var prop in $scope.filter)
            {
                if (noSubFilter($scope.filter[prop]))
    continue;
                if (!$scope.filter[prop][party[prop]])
                {
                    matchesAND = false;
                    break;
                }
            }
            return matchesAND;
        };

    function noSubFilter(subFilterObj)
    {
        for (var key in subFilterObj)
        {
            if (subFilterObj[key]) return false;
        }
        return true;
    }
    });

weddingApp.controller('FilterTestCtrl', function ($scope, $http)
{
    $http.get('/groupings').success(function (data)
    {
        console.log('hi');
        $scope.groupings = data;
        console.log($scope.groupings);

    }).error(function (data)
    {
        console.log('nope');
    });

    $scope.filter = {};

    $scope.getOptionsFor = function (propName)
    {
        // console.log(propName);
        var list = $scope.groupings[propName];
        // console.log(list);
        return ($scope.groupings[propName] || [])
        // .map(function (p)
        // {
        //     console.log(p["ok"]);
        //     console.log(p[propName]);
        //     console.log(p);
        // });
        .filter(function (p, idx, arr)
        {
            return arr.indexOf(p) === idx;
        });
    };

    $scope.filterByProperties = function (party)
    {
        var matchesAND = true;
        for (var prop in $scope.filter)
        {
            if (noSubFilter($scope.filter[prop]))
continue;
            if (!$scope.filter[prop][party[prop]])
            {
                matchesAND = false;
                break;
            }
        }
        return matchesAND;
    };

    function noSubFilter(subFilterObj)
    {
        for (var key in subFilterObj)
        {
            if (subFilterObj[key]) return false;
        }
        return true;
    }
});

weddingApp.filter('capitalizeFirst', function ()
{
    return function (str)
    {
        str = str || '';
        return str.substring(0,1).toUpperCase() +
            str.substring(1).toLowerCase();
    };
});
// if ;you can't get it just make them their own queries

// weddingApp.directive('partyCard', function ($http)
// {
//     function link($scope, $elem, attrs)
//     {
//         console.log(attrs);
//         $http.get('/view/parties').success(function (data)
//         {
//             console.log(data);
//             $scope.parties = data;
//         }).error(function (data)
//         {
//             console.log('error');
//         });
//     }
//     return {
//         link: link,

//     };
// });