angular.module('ionicApp', [])

.service('MentorFinder', function() {
    return {
        get: function () {
            const ionItems = document.querySelectorAll('#mentor_list ion-items');

            return Array.from(ionItems).map(ii => ii.innerHTML);
        }
    }
})

.controller('pageController', function($scope, MentorFinder) {

    var mentors = MentorFinder.get();

    $scope.data = {
        mentors: mentors,
        searchQuery: ''
    };

    $scope.findMentors = function () {
        var searchQuery = $scope.data.searchQuery.toLowerCase();

        $scope.data.mentors = $scope.data.mentors
            .filter(mentor => mentor.toLowerCase().indexOf(searchQuery) !== -1);
    }

    $scope.clearSearch = function () {
        $scope.data.searchQuery = '';
    }
})
