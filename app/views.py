from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from dataclasses import dataclass
# Create your views here.
@dataclass
class Team:
    Name: str
    Description: str
    Team_Members: list[str]


Teams = {
    "management": Team(  
        "Management",
        "Management team is in charge of keeping base camp clean and keeping people on schedule",
        ["Owen", "Jeremiah", "Nick", "Ab", "Abigail", "Mathew"],
    ),
    "community": Team(
        "Community",
        "Community team is in charge of team building events which help classmates get to know each other and builds teamwork",
        ["Jordan", "Joby", "Aj", "Micah", "Caleb"],
    ),
    "documentation": Team(
        "Documentation",
        "Documentation team is in charge of documenting the base camp experience by photos and videos they also have control over the social media pages",
        [
            "Conner",
            "Kaleigh",
            "Blair",
            "Mina",
            "Jay",
            "Joshua",
            "Kayleah",
        ],
    ),
    "procurement": Team(
        "Procurement",
        "Procurement is in charge of the school's lunch and cleaning supplies budget they are also in charge of preparing lunch",
        ["Adrian", "Bryce", "Big John", "Blaine", "Wyatt"],
    ),
}

def main_page(request: HttpRequest)->render:
    context={
        "lteam" : Teams.keys
    }  
    return render(request, "index.html", context)  

def info_page(request: HttpRequest, team_name: str) ->render:
    context = {
        "team_info" : Teams[team_name]
    }
    return render(request,"info.html", context)
 