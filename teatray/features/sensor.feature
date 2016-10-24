Feature: I want to use sensors to control the audio
As a BSP user
I want to be able to touch a tile
So that I hear some audio


  Scenario: I touch a tile, I hear audio
    Given I am not touching a tile
    When I press tile "25"
    Then I can receive a response

  Scenario: Change file when sensor changes
    Given I am touching tile "25"
    When I press tile "26"
    Then I can recieve a response
