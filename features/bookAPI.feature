Feature: Verify if Books are added and deleted using Library API
# @ = tag / annotation

#  @smoke
#    Scenario: Verify AddBook API Library
#      Given the Book details which needs to be added to library
#      When we execute the AddBook PostAPI method
#      Then book is successfully added

  @booklibrary
    Scenario: Verify AddBook API Library
      Given the Book details which needs to be added to library
      When we execute the AddBook PostAPI method
      Then book is successfully added
      And status code of response should be 200


    @booklibrary
#     jika ingin membuat parameter pengujian dengan beberapa dataset
    Scenario Outline: Verify AddBook API Library
      Given the Book details with <isbn> and <aisle>
      When we execute the AddBook PostAPI method
      Then book is successfully added
      Examples:
        | isbn | aisle|
        |asdf  | 123  |
        |zxcv  | 456  |
#      1 baris dataset = 1 scenario, kalau 2 baris dataset = 2 scenario
