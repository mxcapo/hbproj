'use strict';

/** App Module Init **/
var weddingApp = angular.module('weddingApp', ['ngRoute', 'weddingAppControllers']);

weddingApp.config(function ($routeProvider, $interpolateProvider)
    {
        $routeProvider.when('/view/parties',
        {
            templateUrl: "../static/partials/partycard.html",
            controller: "PartyListCtrl"
        }).when('/view',
        {
            templateUrl: "../static/partials/f2.html",
            controller: "FilterCtrl"
        }).when('/filtertest',
        {
            templateUrl: "../templates/filtertest.html",
            controller: "FilterTestCtrl"
        }).otherwise(
        {
            redirectTo:"/"
        });
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    });