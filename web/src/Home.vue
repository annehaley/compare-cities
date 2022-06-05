<script lang="ts">
import {
  defineComponent, ref, computed
} from '@vue/composition-api';
import { cities } from './store';
import { City, Marker } from './types';

export default defineComponent({
  setup() {
    const center = ref({ lat: 37.09, lng: -95.713 });
    const markerLocations = computed(
      (): Marker[] =>cities.value.map(
        (city: City) => (
          {
            position: {lat: city.latitude, lng: city.longitude},
            id: city.id,
          }
        )
      )
    )
    return {
      center,
      markerLocations,
    }
  }
});
</script>

<template>
  <GmapMap
    :center='center'
    :zoom='5'
    style='width:100%;  height: 100%;'
  >
    <GmapMarker
      v-for="marker in markerLocations"
      :key="marker.id"
      :position="marker.position"
      @click="center=marker.position"
    />
  </GmapMap>
</template>
