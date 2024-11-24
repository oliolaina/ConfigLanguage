import pytest
import json
import unittest
import os
from main import parse_json

def test_conf1():
    output = """C configuration example
(def comment "configuration example")
(def player table(
name => "Player1",
health => "100",
level => "1",
inventory => table(
weapon => "sword",
items => "potion"
)
))"""
    file = "config1.json"
    with open(file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    assert parse_json(json_data) == output


def test_conf2():
    output = """C constant calculation
(def comment "constant calculation")
(def constant_1 123)
(def constant_2 "hello")
(def constant_3 "hello")
(def constant_4 123)"""
    file = "config2.json"
    with open(file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    assert parse_json(json_data) == output


def test_conf3():
    output = """(def name "Городская библиотека")
(def location "Москва, Россия")
(def book1 table(
title => "Война и мир",
author => "Лев Толстой",
published_year => 1869,
genre => "роман-эпопея",
availability => table(
available_copies => 3,
total_copies => 10
)
))
(def book2 table(
title => "1984",
author => "Джордж Оруэлл",
published_year => 1949,
genre => "роман",
availability => table(
available_copies => 0,
total_copies => 5
)
))
(def book3 table(
title => "Мастер и Маргарита",
author => "Михаил Булгаков",
published_year => 1967,
genre => "фантастика",
availability => table(
available_copies => 2,
total_copies => 7
)
))"""
    file = "config3.json"
    with open(file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    assert parse_json(json_data) == output