using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TurkTelekom.Case.Dtos.GenresDtos;
using TurkTelekom.Case.Dtos.Interfaces;

namespace TurkTelekom.Case.Dtos.MovieDtos
{
    public class MovieListDto : IDto
    {
        public int id { get; set; }
        public List<int> genre_ids { get; set; }
        public List<GenresListDto> genres { get; set; }
        public string original_title { get; set; }
        public string name { get; set; }
        public string original_language { get; set; }
        public string title { get; set; }
        public int vote_count { get; set; }
        public string poster_path { get; set; }
        public string backdrop_path { get; set; }
        public float vote_average { get; set; }
        public string overview { get; set; }
        public int runtime { get; set; }
    }
}
