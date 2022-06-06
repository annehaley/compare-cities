<script lang="ts">
import {
  defineComponent, ref, computed
} from '@vue/composition-api';
import { cities } from './store';
import { City, Marker } from './types';

export default defineComponent({
  setup() {
    const center = ref({ lat: 37.09, lng: -95.713 });
    const highlightedCity = ref<City>()
    const highlightInfo = [
      'population',
      'density',
      'total_employment',
      'average_wages_and_salaries',
      'per_capita_dividends_interest_and_rent',
      'per_capita_personal_income',
      'per_capita_net_earnings',
      'incorporated',
      'military',
    ]
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
    function highlightCity(marker: Marker){
      center.value = marker.position;
      highlightedCity.value = cities.value.find(
        (city: City) => city.id === marker.id
      )
    }
    function getProperty<T, K extends keyof T>(o: T, propertyName: K): T[K] {
        return o[propertyName];
    }
    return {
      center,
      markerLocations,
      highlightedCity,
      highlightInfo,
      highlightCity,
      getProperty,
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
      @click="() => highlightCity(marker)"
    />
    <GmapInfoWindow
      v-if="highlightedCity"
      :opened="highlightedCity"
      :position="({lat: highlightedCity.latitude, lng: highlightedCity.longitude})"
    >
      <v-card width="400px">
        <v-card-title>
          {{ highlightedCity.name }}, {{ highlightedCity.state_id }}
        </v-card-title>
        <v-card-subtitle>
          {{ highlightedCity.county_name }} County
        </v-card-subtitle>
        <v-container>
          <v-row
            v-for="attribute in highlightInfo"
            :key="attribute"
            class="d-flex"
            no-gutters
          >
            <v-col cols="9" class="font-weight-bold">{{ attribute.replace(/_/g, ' ') }}</v-col>
            <v-col cols="3">{{ getProperty(highlightedCity, attribute) }}</v-col>
          </v-row>

        </v-container>
      </v-card>
    </GmapInfoWindow>
  </GmapMap>
</template>
