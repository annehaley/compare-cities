<script lang="ts">
import {
  defineComponent,
} from '@vue/composition-api';

// Initialize and add the map
function initMap(): void {
  // The location of Uluru
  const uluru = { lat: -25.344, lng: 131.031 };
  // The map, centered at Uluru
  const map = new google.maps.Map(
    document.getElementById("map") as HTMLElement,
    {
      zoom: 4,
      center: { lat: 37.09, lng: -95.713 },
    }
  );

  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    position: uluru,
    map: map,
  });
}

declare global {
  interface Window {
    initMap: () => void;
  }
}
window.initMap = initMap;

export default defineComponent({
  setup() {
    return {}
  }
});
</script>

<template>
  <div id="map" class="map"></div>
</template>

<style scoped>
.map {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
  overflow: hidden;
}
</style>
