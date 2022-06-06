<script lang="ts">
import { City } from '@/types';
import { defineComponent, ref, computed } from '@vue/composition-api'
import { allCities, cities, pointSelection, pointSelectionMode } from '../store';
import distance from '../utils/distance'
import getProperty from '@/utils/property';

export default defineComponent({
    setup() {
        const rangeFilters = {
            'population': "Population",
            'density': "Density",
            'total_employment': "Employment",
            'average_wages_and_salaries': "Avg wages & salaries",
            'per_capita_personal_income': "Personal income",
            'per_capita_dividends_interest_and_rent': "Net costs",
            'per_capita_net_earnings': "Net earnings",
        }
        const maximumRanges = computed(() => {
            return Object.fromEntries(
            Object.entries(rangeFilters).map(
                ([attribute,]) => {
                    const allValues: number[] = allCities.value.map(
                        (city: City) => getProperty(city, attribute as keyof City) || -1
                    ).filter((value) => value > 0)
                    let min = Math.min(...allValues)
                    let max = Math.max(...allValues)
                    min = min > 0 ? min :0
                    max = max < 5000000000 ?max :5000000000
                    return [attribute, [min, max]]
                }
            )
        )})
        const selectedRanges = ref(Object.assign({}, maximumRanges.value))
        const milesFrom = ref<number>(10)
        const includeMilitary = ref<Boolean>(true)
        const includeUnincorporated = ref<Boolean>(true)


        function filter() {
            cities.value = allCities.value
            if(pointSelection.value && milesFrom.value){
                cities.value = cities.value.filter(
                    (city: City) => distance(
                        pointSelection.value.lat,
                        city.latitude,
                        pointSelection.value.lng,
                        city.longitude,
                    ) < milesFrom.value
                )
            }
            Object.entries(selectedRanges.value).forEach(
                ([attribute, range]) => {
                    cities.value = cities.value.filter(
                        (city: City) => {
                            const value = getProperty(city, attribute as keyof City)
                            if(value === 'N/A') return true
                            return value <= range[1] && value >= range [0]
                        }
                    )
                }
            )
            if(!includeMilitary.value) {
                cities.value = cities.value.filter(
                    (city) => !city.military
                )
            }
            if(!includeUnincorporated.value) {
                cities.value = cities.value.filter(
                    (city) => city.incorporated
                )
            }
        }

        return {
            pointSelection,
            pointSelectionMode,
            rangeFilters,
            milesFrom,
            selectedRanges,
            maximumRanges,
            includeMilitary,
            includeUnincorporated,
            filter,
        }
    },
})
</script>


<template>
    <v-navigation-drawer
        absolute
        permanent
    >
    <v-card color="transparent" flat>
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
                </v-container>
            </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel
            v-for="(range, attribute) in maximumRanges"
            :key="attribute"
        >
            <v-expansion-panel-header>
                {{ rangeFilters[attribute] }}
            </v-expansion-panel-header>
            <v-expansion-panel-content>
                <v-range-slider
                    v-model="selectedRanges[attribute]"
                    class="mt-5"
                    thumb-label="always"
                    :min="range[0]"
                    :max="range[1]"
                    step="10"
                />
            </v-expansion-panel-content>
        </v-expansion-panel>
        <v-checkbox
            v-model="includeMilitary"
            label="Include Military Cities"
        />
        <v-checkbox
            v-model="includeUnincorporated"
            label="Include Unincorporated Cities"
        />
        <v-btn color="primary" @click="filter" class="mt-5">
            Filter
        </v-btn>
        </v-expansion-panels>
    </v-card>
    </v-navigation-drawer>
</template>
