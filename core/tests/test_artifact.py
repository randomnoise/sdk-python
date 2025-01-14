import pytest
from cdevents.core.artifact import (
    ArtifactEvent,
    ArtifactPackagedEvent,
    ArtifactPublishedEvent,
)
from cdevents.core.event_type import EventType


@pytest.mark.unit
def test_artifact_created():
    artifact_event = ArtifactEvent(
        artifact_type=EventType.ArtifactPackagedEventV1,
        id="_id",
        name="_name",
        version="_version",
        data={"key1": "value1"},
    )
    assert artifact_event is not None
    assert artifact_event._attributes["type"] == EventType.ArtifactPackagedEventV1.value
    assert artifact_event._attributes["extensions"] == {
        "artifactid": "_id",
        "artifactname": "_name",
        "artifactversion": "_version",
    }
    assert artifact_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_artifact_type_packaged_v1():
    artifact_event = ArtifactPackagedEvent(
        id="_id", name="_name", version="_version", data={"key1": "value1"}
    )
    assert artifact_event is not None
    assert artifact_event._attributes["type"] == EventType.ArtifactPackagedEventV1.value
    assert artifact_event._attributes["extensions"] == {
        "artifactid": "_id",
        "artifactname": "_name",
        "artifactversion": "_version",
    }
    assert artifact_event.data == {"key1": "value1"}


@pytest.mark.unit
def test_artifact_type_published_v1():
    artifact_event = ArtifactPublishedEvent(
        id="_id", name="_name", version="_version", data={"key1": "value1"}
    )
    assert artifact_event is not None
    assert artifact_event._attributes["type"] == EventType.ArtifactPublishedEventV1.value
    assert artifact_event._attributes["extensions"] == {
        "artifactid": "_id",
        "artifactname": "_name",
        "artifactversion": "_version",
    }
    assert artifact_event.data == {"key1": "value1"}
