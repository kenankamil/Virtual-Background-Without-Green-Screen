using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TurkTelekom.Case.Dtos.Interfaces;

namespace TurkTelekom.Case.Dtos.GenresDtos
{
   public class GenresListDto : IDto
    {
        public int id { get; set; }
        public string name { get; set; }
    }
}
