export type HazardCategory = 'Flood' | 'Icy' | 'Air quality' | 'Construction' | 'Damaged road';
export type HazardStatus = 'Pending' | 'Approved' | 'Rejected';
export type Hazard = { id: number; category: HazardCategory; title: string; description: string; area: string; severity: 'High' | 'Medium' | 'Low'; source: string; date: string; status: HazardStatus; photo?: boolean };
export type ParkingLot = { id: number; name: string; free: number | null; capacity: number; updated: string; location: string; history: number[] };
export type CityEvent = { id: number; name: string; place: string; date: string; time: string; category: string; outdoors: boolean; organizer: string; status: HazardStatus };
export const initialParking: ParkingLot[] = [
  { id: 1, name: 'Khan Shatyr lot', free: 42, capacity: 120, updated: '1 min ago', location: 'Khan Shatyr', history: [102, 84, 69, 51, 42] },
  { id: 2, name: 'Esil Boulevard lot', free: 18, capacity: 80, updated: '2 min ago', location: 'Esil Boulevard', history: [72, 61, 49, 31, 18] },
  { id: 3, name: 'Baiterek lot', free: 3, capacity: 60, updated: '1 min ago', location: 'Baiterek', history: [46, 32, 21, 9, 3] },
  { id: 4, name: 'Station Square lot', free: null, capacity: 50, updated: '14 min ago', location: 'Station Square', history: [35, 31, 26, 24, 21] },
];
export const initialHazards: Hazard[] = [
  { id: 1, category: 'Icy', title: 'Icy road: Respubliki Ave bridge', description: 'Black ice on the bridge deck and approaches. Reduce speed.', area: 'Respubliki Ave', severity: 'High', source: 'administrator', date: '23 Oct, 09:10', status: 'Approved' },
  { id: 2, category: 'Flood', title: 'Flood-prone area: Ishim embankment', description: 'Water level above seasonal norm. Lower embankment paths may be closed.', area: 'Ishim river', severity: 'Medium', source: 'administrator', date: '21 Oct, 12:00', status: 'Approved' },
  { id: 3, category: 'Air quality', title: 'Air quality hotspot: left-bank industrial zone', description: 'Elevated particulate readings reported for the area.', area: 'Left-bank industrial zone', severity: 'Medium', source: 'administrator', date: '20 Oct, 08:30', status: 'Approved' },
  { id: 4, category: 'Construction', title: 'Roadworks: Kabanbay Batyr St', description: 'One lane closed between two junctions until 30 Oct.', area: 'Kabanbay Batyr St', severity: 'Low', source: 'administrator', date: '18 Oct, 10:00', status: 'Approved' },
  { id: 5, category: 'Icy', title: 'Ice under the snow at the bus stop on Abay Ave.', description: 'Ice under the snow at the bus stop on Abay Ave.', area: 'Abay Ave', severity: 'High', source: 'Citizen', date: '23 Oct, 14:02', status: 'Pending', photo: true },
  { id: 6, category: 'Flood', title: 'Water about 20 cm deep in the Saryarka underpass.', description: 'Water about 20 cm deep in the Saryarka underpass.', area: 'Saryarka underpass', severity: 'Medium', source: 'Citizen', date: '23 Oct, 15:40', status: 'Pending' },
];
export const initialEvents: CityEvent[] = [
  { id: 1, name: 'Ice Sculpture Festival', place: 'Presidential Park', date: '28 Oct', time: '12:00–20:00', category: 'Culture', outdoors: true, organizer: 'Aigerim S.', status: 'Pending' },
  { id: 2, name: 'Astana City Run', place: 'Botanical Garden', date: '26 Oct', time: '08:00–11:00', category: 'Sport', outdoors: true, organizer: 'City Sports Office', status: 'Approved' },
  { id: 3, name: 'Local Makers Market', place: 'EXPO grounds', date: '29 Oct', time: '10:00–18:00', category: 'Market', outdoors: false, organizer: 'Astana Events', status: 'Approved' },
];
export const hazardCategories: HazardCategory[] = ['Flood', 'Icy', 'Air quality', 'Construction', 'Damaged road'];
