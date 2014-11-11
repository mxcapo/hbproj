'use strict';

/** App Module Init **/
var weddingApp = angular.module('weddingApp', ['ngRoute', weddingAppControllers]);

weddingApp.config(function ($routeProvider, $interpolateProvider)
    {
        $routeProvider.when('/view/parties',
        {
            templateUrl: "../static/partials/partycard.html",
            controller: "PartyListCtrl"
        }).otherwise(
        {
            redirectTo: '/'
        });
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    });