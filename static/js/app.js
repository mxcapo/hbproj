'use strict';

/** App Module Init **/
var weddingApp = angular.module('weddingApp', ['ngRoute', 'weddingAppControllers']);

weddingApp.config(function ($routeProvider, $interpolateProvider)
    {
        // $routeProvider.when('/')
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    });