<script lang="ts">
import { City } from '@/types';
import { defineComponent, ref } from '@vue/composition-api'
import { cities, pointSelection, pointSelectionMode } from '../store';
import { distance } from '../utils/distance'

export default defineComponent({
    setup() {
        const milesFrom = ref<number>(10)
        function filterMilesFrom() {
            cities.value = cities.value.filter(
                (city: City) => distance(
                    pointSelection.value.lat,
                    city.latitude,
                    pointSelection.value.lng,
                    city.longitude,
                ) < milesFrom.value
            )
        }
        return {
            milesFrom,
            pointSelection,
            pointSelectionMode,
            filterMilesFrom,
        }
    },
})
</script>


<template>
    <v-navigation-drawer
        absolute
        permanent
    >
    <v-card height="100%">
        <v-card-title>
            Filters
        </v-card-title>
        <v-expansion-panels>
        <v-expansion-panel>
            <v-expansion-panel-header>
                Distance To...
            </v-expansion-panel-header>
            <v-expansion-panel-content>
                <v-btn
                    v-if="!pointSelectionMode && !pointSelection"
                    @click="pointSelectionMode = true"
                >
                    Select location
                </v-btn>
                <v-btn
                    v-else-if="pointSelection"
                    @click="pointSelection = undefined; pointSelectionMode = false"
                >
                    Clear location
                </v-btn>
                <v-container v-if="pointSelection" class="mt-7">
                    <v-slider
                        v-model="milesFrom"
                        step="10"
                        min="10"
                        max="200"
                        thumb-label="always"
                        ticks="always"
                        tick-size="4"
                    />
                    miles from
                    ({{ pointSelection.lat }}, {{ pointSelection.lng }})
                    <br />
                    <v-btn color="primary" @click="filterMilesFrom">
                        Filter
                    </v-btn>
                </v-container>
            </v-expansion-panel-content>
        </v-expansion-panel>
        </v-expansion-panels>
    </v-card>
    </v-navigation-drawer>
</template>
