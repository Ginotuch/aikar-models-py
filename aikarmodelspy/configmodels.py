from typing import Optional

from pydantic import BaseModel, Field

from aikarmodelspy.aikarmodel import AikarObject


class Ticks(AikarObject):
    timed_ticks: int = Field(alias="timedTicks")
    player_ticks: int = Field(alias="playerTicks")
    activated_entity_ticks: int = Field(alias="activatedEntityTicks")
    tile_entity_ticks: int = Field(alias="tileEntityTicks")


class FullServerTick(AikarObject):
    id: int
    count: int
    total: int
    lag_count: int = Field(alias="lagCount")
    lag_total: int = Field(alias="lagTotal")


class MinuteReport(AikarObject):
    time: int
    tps: int
    avg_ping: int = Field(alias="avgPing")
    full_server_tick: FullServerTick = Field(alias="fullServerTick")
    ticks: Ticks


class Region(AikarObject):
    region_id: str = Field(alias="regionId")
    chunk_count: int = Field(alias="chunkCount")
    area_loc_x: int = Field(alias="areaLocX")
    area_loc_z: int = Field(alias="areaLocZ")
    tile_entities: dict[str, int] = Field(alias="tileEntities")
    entities: dict[str, int]


class WorldData(AikarObject):
    world_name: str = Field(alias="worldName")
    regions: dict[str, Region]


class Data(AikarObject):
    id: int
    start: int
    end: int
    total_ticks: int = Field(alias="totalTicks")
    total_time: int = Field(alias="totalTime")
    world_data: dict[str, WorldData] = Field(alias="worldData")
    minute_reports: list[MinuteReport] = Field(alias="minuteReports")


class Plugin(AikarObject):
    name: str
    version: str
    description: str
    website: Optional[str]
    authors: str


class Handler(AikarObject):
    name: str
    group: int


class IDMap(AikarObject):
    group_map: dict[str, str] = Field(alias="groupMap")
    handler_map: dict[str, Handler] = Field(alias="handlerMap")
    world_map: dict[str, str] = Field(alias="worldMap")
    tile_entity_type_map: dict[str, str] = Field(alias="tileEntityTypeMap")
    entity_type_map: dict[str, str] = Field(alias="entityTypeMap")


class System(AikarObject):
    timing_cost: int = Field(alias="timingcost")
    name: str
    version: str
    jvm_version: str = Field(alias="jvmversion")
    arch: str
    max_mem: str = Field(alias="maxmem")
    cpu: int
    runtime: int
    flags: str
    gc: dict


class TimingsMaster(AikarObject):
    version: str
    maxplayers: int
    start: int
    end: int
    sample_time: int = Field(alias="sampletime")
    server: str
    motd: str
    online_mode: bool = Field(alias="onlinemode")
    icon: str
    system: System
    idmap: IDMap
    plugins: dict[str, Plugin]
    data: list[Data]
    config: dict


class Config(BaseModel):
    id: str
    timings_master: TimingsMaster = Field(alias="timingsMaster")
