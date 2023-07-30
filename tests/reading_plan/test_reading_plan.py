from tech_news.analyzer.reading_plan import ReadingPlanService
from unittest.mock import patch
import pytest


def test_reading_plan_group_news():
    mock_db = [
        {
            "url": "https://www.tecmundo.com.br/voxel",
            "title": "Voxel",
            "timestamp": "2021-03-18T14:00:00",
            "writer": "João Gabriel",
            "summary": "Resumo",
            "category": "games",
            "reading_time": 5,
        },
        {
            "url": "https://www.tecmundo.com.br/voxel",
            "title": "Voxel",
            "timestamp": "2021-03-18T14:00:00",
            "writer": "João Gabriel",
            "summary": "Resumo",
            "category": "games",
            "reading_time": 10,
        },
        {
            "url": "https://www.tecmundo.com.br/voxel",
            "title": "Voxel",
            "timestamp": "2021-03-18T14:00:00",
            "writer": "João Gabriel",
            "summary": "Resumo",
            "category": "games",
            "reading_time": 15,
        },
    ]

    with patch(
        "tech_news.analyzer.reading_plan.find_news",
        return_value=mock_db,
    ):
        r = ReadingPlanService()
        result = r.group_news_for_available_time(10)

        assert result == {
            "readable": [
                {"chosen_news": [("Voxel", 5)], "unfilled_time": 5},
                {"chosen_news": [("Voxel", 10)], "unfilled_time": 0},
            ],
            "unreadable": [("Voxel", 15)],
        }

        with pytest.raises(ValueError):
            r.group_news_for_available_time(0)
