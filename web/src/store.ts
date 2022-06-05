import axios from 'axios';
import { ref } from '@vue/composition-api';
import { State } from './types';


export const axiosInstance = ref(axios.create({
    baseURL: 'http://localhost:8000/api/v1',
}));

export const searchedStates = ref<State[]>([]);

export const cities = ref([]);

export async function fetchCities(){
    let next_page: number | undefined = 1;
    while(next_page){
        let response = await(axiosInstance.value.get(
            `/cities?states=${searchedStates.value.join(',')}&page=${next_page}`
        ))
        if(response.data.next){
            next_page += 1
        } else {
            next_page = undefined
        }
        cities.value = cities.value.concat(response.data.results)
    }
    console.log(cities.value)
    return cities.value.length
}
