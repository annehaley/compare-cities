<script lang="ts">
import { defineComponent, ref } from '@vue/composition-api';
import FilterSidebar from './components/FilterSidebar.vue';
import ResultsSidebar from './components/ResultsSidebar.vue';
import { searchedStates, fetchCities, cities, allCities } from './store';
import { State } from './types';


export default defineComponent({
  components: { ResultsSidebar, FilterSidebar },
  name: 'App',
  setup() {
    let stateOptions = ref<State[]>([])
    const selectedStates = ref<State[]>([])
    const searching = ref<Boolean>(false)

    async function fetchStateOptions() {
      stateOptions.value = await (await fetch(`states.json`)).json()
    }
    fetchStateOptions()

    async function searchStates() {
      searching.value = true
      searchedStates.value = selectedStates.value
      await fetchCities()
      searching.value = false
    }
    function selectionValid(selection: State[]){
      if (selection.length > 5) return 'Select no more than 5 states'
      return true
    }

    return {
      cities,
      allCities,
      stateOptions,
      selectedStates,
      searchedStates,
      searching,
      searchStates,
      selectionValid
    }
  }
});
</script>

<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
    Compare U.S. Cities
    </v-app-bar>
    <v-overlay
      absolute
      :value="searchedStates.length == 0 || searching"
      :opacity="0.8"
    >
      <v-card width="600px" class="pa-4">
        <v-card-title>Select up to 5 states for your search</v-card-title>
        <v-select
          v-model="selectedStates"
          :items="stateOptions"
          chips
          deletable-chips
          multiple
          item-text="name"
          item-value="abbreviation"
          :rules="[selectionValid]"
        />
        <v-card-actions>
          <v-btn
            @click="searchStates"
            color="primary"
            :disabled="selectedStates.length > 5 || selectedStates.length < 1"
          >
            Search
          </v-btn>
        </v-card-actions>
        <v-progress-linear
          v-if="searching"
          indeterminate
          color="white"
          class="mb-0"
        ></v-progress-linear>
      </v-card>
    </v-overlay>

    <v-main>
      <filter-sidebar v-if="allCities.length"/>
      <router-view />
      <results-sidebar v-if="allCities.length"/>
    </v-main>
  </v-app>
</template>
