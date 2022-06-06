import axios from 'axios';
import { ref } from '@vue/composition-api';
import { State, City, Marker } from './types';


export const axiosInstance = ref(axios.create({
    baseURL: 'http://localhost:8000/api/v1',
}));

export const searchedStates = ref<State[]>([]);

export const allCities = ref<City[]>([]);

export const cities = ref<City[]>([]);

export const highlightedCity = ref<City>()

export const center = ref({ lat: 37.09, lng: -95.713 });

export const infoOpen = ref<Boolean>(false)

export const pointSelection = ref()

export const pointSelectionMode = ref<Boolean>(false)

export function highlightCity(cityId: string){
    highlightedCity.value = cities.value.find(
      (city: City) => city.id === cityId
    )
    if (highlightedCity.value){
        center.value = {lat: highlightedCity.value?.latitude, lng: highlightedCity.value?.longitude};
        infoOpen.value = true
    }
  }

export async function fetchCities(){
    let next_page: number | undefined = 1;
    while(next_page){
        const response = await(axiosInstance.value.get(
            `/cities?states=${searchedStates.value.join(',')}&page=${next_page}`
        ))
        if(response.data.next){
            next_page += 1
        } else {
            next_page = undefined
        }
        cities.value = cities.value.concat(response.data.results)
    }
    allCities.value = cities.value
    return cities.value.length
}
